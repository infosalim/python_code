from time import time

def gen_func(num):
    for i in range(num):
        yield i
t1 = time()
l = []
for i in gen_func(1000000):
    l.append(i)

t2 = time()


m = []
t3 = time()
for i in range(1000000):
    m.append(i)
t4 = time()

print(f'GEN: {t2-t1}')
print(f'REGULAR: {t4-t3}')