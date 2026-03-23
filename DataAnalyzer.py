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
            return np.array(ls, dtype=float)
        except (ValueError, TypeError):
            raise ValueError('Input date must be digit')
    def get_column(self,n):
        if self.data.ndim > 1:
            return self.data[:,n] 
        else:
            print(f"This is 1D array in {self.name} obj")
            return None
    def _np_mean(self):
        return np.mean(np.array(self.data))
    def _np_median(self):
        return np.median(np.array(self.data))
    def _np_std(self):
        return np.std(np.array(self.data))
    def _mean(self):
        flat_data = self.data.flatten()
        return sum(flat_data)/len(flat_data)
    def _median(self):
        flat_data = self.data.flatten()
        ln = len(flat_data)
        sort_ls = sorted(flat_data)
        if ln % 2 == 0:
            return (sort_ls[ln//2 - 1] + sort_ls[ln//2])/2
        else:
            return sort_ls[ln//2]
    def _std(self):
        flat_data = self.data.flatten()
        ln = len(flat_data)
        Mu = self._mean()
        sum_sq = sum((x-Mu)**2 for x in flat_data)
        var = sum_sq/ln
        return var ** 0.5

