from functools import reduce

the_list = [1,2,3,4,5,6]

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(f'Result: {reduce(accumulator, the_list, 0)}')
