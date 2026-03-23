# 1. Standard library imports
import os
from datetime import datetime, timedelta

# 2. Third-party imports
import pandas as pd
import numpy as np
import sys
import timeit



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

        }
        func = mapping.get((param, method))
        if func:
            return func()
        else:
            raise ValueError(f'Problem with parametr or method')
    #preparation method
    def _prep_data(self,ls):
        try:
            proces = [float(x) for x in ls]
            return proces
        except (ValueError, TypeError):
            raise ValueError('Input date must be digit')
    def _np_mean(self):
        return np.mean(np.array(self.data))
    def _np_median(self):
        return np.median(np.array(self.data))
    def _np_std(self):
        return np.std(np.array(self.data))
    def _mean(self):
        return sum(self.data)/len(self.data)
    def _median(self):
        ln = len(self.data)
        sort_ls = sorted(self.data)
        if ln % 2 == 0:
            return (sort_ls[ln//2 - 1] + sort_ls[ln//2])/2
        else:
            return sort_ls[ln//2]
    def _std(self):
        ln = len(self.data)
        Mu = self._mean()
        sum_sq = sum((x-Mu)**2 for x in self.data)
        var = sum_sq/ln
        return var ** 0.5
if __name__ == "__main__":
    args = sys.argv[1:]
    if not args[1:]:
        print('Use: python your_script.py [digit]"')
        sys.exit(1)
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