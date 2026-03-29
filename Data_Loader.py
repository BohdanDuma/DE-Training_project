from pathlib import Path
import os
import sys
import pandas as pd
class DataLoader:
    def __init__(self,name,format='.csv', path_n='.'):
        self.name = name 
        self.format = format 
        self.path = Path(path_n)
class SearchFile(DataLoader):
    def recysion_search(self):
        if self.path == '.':
            print(f"Починаю папку: current")
        else:
            print(f"Починаю папку {self.path}")
        files = list(self.path.rglob("*"+(self.format)))  
        return files
    def __str__(self):
        all_files = self.recysion_search()
        names = [f.name for f in all_files]
        names_formated = ", ".join(names)
        return f"List of {self.format}, len{len(self.recysion_search())}:\n {names_formated}"
class SmartExtractor(SearchFile):
    def extract_by_name(self, target):
        
        all_files = self.recysion_search()
        #Логіка валідатора чи існує такий файл всписку
        full_name = next((f for f in all_files if target in f.name),None)
        if full_name:
            print(f"File was found!")
        else:
            print("no file")
        return full_name
    def smart_logic(self,target, n_col=''):
        full_name = self.extract_by_name(target)
        if not full_name:
            return None, False
        try:
            if self.format == '.csv':
                data = pd.read_csv(full_name)
            elif self.format == '.json':
                data = pd.read_json(full_name)
            else:
                print("Format don't supported")    
                return None, False
            
            return self._prepear_data(data, n_col)
        except Exception as e:
            print(f"Something wrong {e}")
            return None, False
    def _prepear_data(self, data, n_col):
        try:
            two_dem = False
            data_num = data.apply(pd.to_numeric, errors='coerce')
            data_clean = data_num.dropna(axis=1, how='all')
            data_clean = data_clean.dropna(axis=0, how='all')
            if data_clean.empty:
                print("all data wasn't numeric")
                return None
            data_clean = data_clean.to_numpy(dtype=float)

            if n_col == '*':
                    
                arr = data_clean.flatten()
                print('data is 1D arr all col')
            elif isinstance(n_col, int):
                arr = data_clean[:,n_col]
                print('data is 1D arr of n_col index')
            elif data_clean.shape[1] == 1:
                arr = data_clean.flatten()
                print('data 1Darr')
            else:
                arr = data_clean
                two_dem = False
                print('data is matrix')
            arr.flags.writeable = False
            return arr, two_dem
        except Exception as e:
            print(f"Something wrong during preparation: {e}")
            return None, False

dl = SmartExtractor('ex1', '.csv', '/home/bohdan/Стільниця')


print(dl)


result = dl.smart_logic('1111', )


final_data, is_matrix = result
print(f"Final shape: {final_data.shape}, Is Matrix: {is_matrix}")