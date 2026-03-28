# 1. Standard library imports
import os
from datetime import datetime, timedelta
import time 
from functools import wraps, lru_cache

# 2. Third-party imports
import pandas as pd
import numpy as np
import sys
import timeit

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"method {func.__name__} run for {end - start:.6f}sec")
        return result
    return wrapper
class DataAnalyzer:
    def __init__(self, name, ls):
        self.name = name
        self.data = self._prep_data(ls)
    #dispatcher method
    def get_method(self, param='mean', method='manual'):
        '''
        param: 'mean', 'median', 'std'
        method: 'mmanual', 'numpy'
        '''
        mapping = {
            ('mean', 'manual'): self._mean,
            ('mean', 'numpy'): self._np_mean,
            ('median', 'manual'): self._median,
            ('median', 'numpy'): self._np_median,
            ('std', 'manual'): self._std,
            ('std', 'numpy'): self._np_std,
            ('bubble_sort','manual'): self._buble_sort,
            ('merge_sort','manual'): self._merge_sort,
            ('sort','manual'): self._python_sort,
            ('sort','numpy'): self._numpy_sort,
        }
        func = mapping.get((param, method))
        if func:
            return func()
        else:
            raise ValueError(f'Problem with parametr or method')
    
    @time_it
    def _np_mean(self):
        return np.mean(np.array(self.data))
    @time_it
    def _np_median(self):
        return np.median(np.array(self.data))
    @time_it
    def _np_std(self):
        return np.std(np.array(self.data))
    @time_it
    def _mean(self):
        flat_data = self.data.flatten()
        return sum(flat_data)/len(flat_data)
    @time_it
    def _median(self):
        flat_data = self.data.flatten()
        ln = len(flat_data)
        sort_ls = sorted(flat_data)
        if ln % 2 == 0:
            return (sort_ls[ln//2 - 1] + sort_ls[ln//2])/2
        else:
            return sort_ls[ln//2]
    @time_it
    def _std(self):
        flat_data = self.data.flatten()
        ln = len(flat_data)
        Mu = self._mean()
        sum_sq = sum((x-Mu)**2 for x in flat_data)
        var = sum_sq/ln
        return var ** 0.5
    @time_it
    def _merge_sort(self):
        flat_data = self.data.flatten().tolist()
        def _merge_sorting(ls):
            if len(ls) <= 1:
                return ls
            mid = len(ls) // 2
            left = _merge_sorting(ls[:mid])
            right = _merge_sorting(ls[mid:])
            return merge(left, right)
        def merge(left, right):
            result = []
            i = j =0 
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        return _merge_sorting(flat_data)
        
    @time_it
    def _buble_sort(self):
        flat_data = self.data.flatten().tolist()
        n = len(flat_data)
        for i in range(n):
            for j in range(0, n-i-1):
                if flat_data[j] > flat_data[j + 1]:
                    flat_data[j], flat_data[j + 1] = flat_data[j + 1], flat_data[j]
        return flat_data
    @time_it
    def _numpy_sort(self):
        return np.sort(self.data)
    @time_it
    def _python_sort(self):
        flat_data = sorted(self.data.flatten())
        return flat_data
    def column(self, n_col = 0, all_col=False):
        try:
            if self.data.ndim > 1:
                if all_col:
                    return [self.data[:,i] for i in range(self.data.shape[1])]
            if n_col >= self.data.shape[1]:
                raise IndexError(f"array doesn't have {n_col}")
            return [self.data[:,n_col]]  
            if all_col:
                return [self.data]
            return self.data
        except IndexError:
            print("array doesn't have {n_col}")
            return None
        except Exception as e:
            print(f"uncnown {e}")
            return None
class TimeSerialsAnalyzer(DataAnalyzer):
    def __init__(self, name, ls):
        super().__init__(name, ls) 
        self.data.flags.writeable = False
    @time_it
    @lru_cache(maxsize=None) 
    def sma(self, win=3):
        if win > len(self.data) or win <= 0:
            return np.array([])
        window = np.ones(win)
        return np.convolve(self.data, window,mode='valid') / win 
if __name__ == "__main__":
    rng = np.random.default_rng()
    arr1 = rng.random(10)
    arr3 = rng.random(100)
    arr2 = rng.random(10000)
    test_sort = DataAnalyzer('Sorting', arr1)
    test_sort_2 = DataAnalyzer('Sorting', arr2)
    test_sort._buble_sort()
    test_sort._merge_sort()
    test_sort_2._buble_sort()
    test_sort_2._merge_sort()
    test_sort._python_sort()
    test_sort._numpy_sort()
    test_sort_2._python_sort()
    test_sort_2._numpy_sort()
    test_sma_obj = TimeSerialsAnalyzer('SMA', arr3)
    test_sma_obj.sma(3)
    test_sma_obj.sma(3)
    test_sma_obj.sma(3)