import sys
import json
import timeit
from DataAnalyzer import DataAnalyzer
def benchmark_for_num_and_man(data):
    try:
        numeric_data = [float(x) for x in data]
    except ValueError:
        print("Error: For benchmark, provide a list of numbers.")
        return
    analyzer = DataAnalyzer('BashTest',args)
    res_m = analyzer.get_method('std', 'manual')
    res_n = analyzer.get_method('std', 'numpy')
    print(f"--- Analyz {analyzer.name} ---")
    print(f"Manual STD: {res_m:.5f}")
    print(f"NumPy STD:  {res_n:.5f}")
    t_m = timeit.timeit(lambda: analyzer.get_method('std', 'manual'), number=100)
    t_n = timeit.timeit(lambda: analyzer.get_method('std', 'numpy'), number=100)
    print(f"\nTime (100 iteration):")
    print(f"Manual: {t_m:.5f} sec")
    print(f"NumPy:  {t_n:.5f} sec")   
def extractor_test(args):
    if len(args)<2: return
    try:
        # Чекаємо рядок вигляду: '[[1,2],[3,4]]'
        input_data = json.loads(args)
        da = DataAnalyzer("BashMatrix", input_data)
        
        # Тестуємо 1-й стовпець (індекс 0)
        col = da.get_column(0)
        print(f"--- SQL SELECT col_0 FROM {da.name} ---")
        print(col)
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
        benchmark_for_num_and_man(args)

        
    
    