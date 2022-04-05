from functools import reduce

the_list = [1,2,3,4,5,6,7,8,9]

# print(list(map(lambda item: item*2, the_list)))
# print(list(filter(lambda item: item%2 == 0, the_list)))
# print(reduce(lambda acc,item: acc+item, the_list, 0))

# List Square 
new_list = list(map(lambda num: num**2, the_list))
print(new_list)

# List Sorting 
a = [(0,2), (4,3),(10, -1), (9, 9)]
a.sort(key=lambda x: x[1])

print(a)