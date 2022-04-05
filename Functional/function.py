def multiply(li, mul):
    new_list = []
    for item in li:
        new_list.append(item*mul)
    
    return new_list

the_list = [1,2,3,4,5, 6]
another_list = [10,20,30,40,50]
another_one = [11,22,33,44,55]
# print(multiply(the_list, 3))

def mul(li):
    return li*2

mapped = list(map(mul, [1,2,3]))

def only_odd(item):
    return item % 2 != 0

filtered = list(filter(only_odd, [1,2,3,4,5,6,7,8,9]))
# print(filtered)

zipped = list(zip(the_list, another_list, another_one))
print(zipped)