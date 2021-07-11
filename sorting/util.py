# decorator:  add new functionality to an existing object without modifying its structu
 
import time
def time_it(func):
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        end = time.time()
        print(func.__name__ + " took" + str((end-start)*1000) + " mil sec")
        return result
    return wrapper