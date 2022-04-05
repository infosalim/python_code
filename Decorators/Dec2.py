from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1}ms')
        return result
    return wrapper


@performance
def long_time(num):
    for i in range(num):
        i*2

long_time(1000)