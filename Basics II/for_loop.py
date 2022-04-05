# user = {
#     'name': 'Salim',
#     'surename': 'Hossain',
#     'age': 23
# }

# for item in 'salim':
#     print(item)


# for item in user.keys():
#     print(item)

# my_list = [1,2,3,4,5,6,7,8,9,10]
# total_item = 0;
# for item in my_list:
#     total_item = total_item + item

# print(total_item)

# Range - range() 

# for _ in range(0,2):
#     print(list(range(10)))

# enumerate() - usefull for counting index
# for i, char in enumerate('Hossain'):
# for i, char in enumerate([1,2,3,4,5,6,7,8,9]):
#     print(i, char)

for i, char in enumerate(list(range(100))):
    if char==50:
        print(f'index of 50 is: {i}')