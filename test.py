import sys
import json
import timeit
from DataAnalyzer import DataAnalyzer
>>>>>>def run_cli():
    args = sys.argv[1:]
    if not args:
        print("Error: there isn't data for analyze")
        return
    try:
        if args[0].startswith('['):
            data = json.loads(args)
            da = DataAnalyzer("Matrixdata", data)
            # Info about col
            cols = da.data.shape[1] if da.data.ndim > 1 else 1
            <<<<<<<

def benchmark_for_num_and_man(data):
    analyzer = DataAnalyzer('BashTest',data)
    res_m = analyzer.get_method('std', 'manual')
    res_n = analyzer.get_method('std', 'numpy')
    print(f"--- Analyz {analyzer.name} ---")
    print(f"Manual STD: {res_m:.5f}")
    print(f"NumPy STD:  {res_n:.5f}")

def extractor_test(args):
    if len(args)<2: return
    try:
        # Чекаємо рядок вигляду: '[[1,2],[3,4]]'
        input_data = json.loads(args)
        da = DataAnalyzer("BashMatrix", input_data)
        # Does it see columns
        num_col = da.data.shape(1)
        print(f"Object {da.name} has {num_col} columns")
    except Exception as e:
        print(f"Error in extractor: {e}") # Якщо в аргументах не JSON     
if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print('Use: python test.py "[1,2,3]" OR python test.py 1 2 3')
        sys.exit(1)
    if args[0].startswith('['):
        extractor_test(args[0])
        
    else:
        try:
            # Конвертуємо ТУТ, перед викликом функції
            numeric_args = [float(x) for x in args]
            benchmark_for_num_and_man(numeric_args)
        except ValueError:
            print("Error: For benchmark, provide a list of numbers.")

        
    
    