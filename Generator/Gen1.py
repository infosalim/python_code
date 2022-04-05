from time import time

# print(list(range(10)))

# t1 = time()
def gen_func(num):
    for i in range(num):
        yield i*2

g = gen_func(100)
print(g)
# next(g)
# next(g)
# next(g)
# print(next(g))

# t2 = time()
# for item in gen_func(10000):
#     print(item)
# print(f'Gen: {t2-t1}')

# def make_list(num):
#     res = []
#     t1 = time()
#     for i in range(num):
#         res.append(i)
#     t2 = time()
#     print(f'Make: {t2-t1}')
#     return res

# make_list = make_list(10000)

make_list2 = gen_func(10000)