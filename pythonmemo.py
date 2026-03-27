from functools import lru_cache
from functools import wraps
import time

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args,**kwargs)
        end = time.perf_counter()
        print(f"method {func.__name__} run for {end - start:.6f}sec")
        return result
    return wrapper

@lru_cache(maxsize=None) 
def Fibonachi_memo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonachi_memo(n-1) + Fibonachi_memo(n-2)

@time_it
def Fibonachi_memo_final(n):
    return Fibonachi_memo(n)
def Fibonachi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonachi(n-1) + Fibonachi(n-2)  
@time_it   
def Fibonachi_final(n):
    return Fibonachi(n)   
print(Fibonachi_final(30),Fibonachi_memo_final(30))

@lru_cache
def Stair_memo(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return Stair(n-1) + Stair(n-2)

@time_it
def Stair_m_f(n):
    return Stair_memo(n)

def Stair(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return Stair(n-1) + Stair(n-2)

@time_it
def Stair_f(n):
    return Stair(n)


print(Stair_m_f(10), Stair_f(10))