from pathlib import Path
import os
import sys

type_dict = {
        '1': '.json',
        '2': '.csv',
        '3': '.txt'
    }
def recysion_search_json(path_f, type_key='1'):
    
    target_ex = type_dict.get(type_key, '.json')
    all_files = []
    print(f"Починаю папку {path_f}")
    try:
        for item in os.listdir(path_f):
            full_path = os.path.join(path_f, item)

            if os.path.isdir(full_path):
                below = recysion_search_json(full_path,type_key)
                all_files.extend(below)
            elif full_path.endswith(target_ex):
                all_files.append(full_path)
    except PermissionError:
        pass
    return all_files
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Помилка: вкажіть тип файлу (1 - json, 2 - csv, 3 - txt)")
        sys.exit(1)
    a = sys.argv[1]
    p = os.getcwd()
    extention = type_dict.get(a)
    list_j = recysion_search_json(p, a)
    print(f'Список з {extention} файлів соформовано. Довжина {len(list_j)}') 