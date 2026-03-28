from pathlib import Path
import os
import sys

class DataLoader:
    def __init__(self,name,format='.csv', path_n=''):
        self.name = name 
        self.format = format 
        self.path = Path(path_n)
class SearchFile(DataLoader):
    def recysion_search(self):
        print(f"Починаю папку {self.path}")
        files = list(self.path.rglob("*"+(self.format)))  
        return files
    def __str__(self):
        all_files = self.recysion_search()
        names = [f.name for f in all_files]
        names_formated = ", ".join(names)
        return f"List of {self.format}, len{len(self.recysion_search())}:\n {names_formated}"
class SmartExtractor(SearchFile):
    def extract_by_name(self, target, n_col=None):
        
        all_files = self.recysion_search()
        #Логіка валідатора чи існує такий файл всписку
        full_name = next((f for f in all_files if target in f.name),None)
        if full_name:
            print(f"File was found!")
        else:
            print("no file")
        return full_name
    def _smart_logic(self, file_path, n_col)

dl = SmartExtractor('ex1','.csv','/home/bohdan/Стільниця')
print(dl)
print(dl.extract_by_name('fighter_popular'))