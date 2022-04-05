# List 
my_list = [char for char in 'hello']
my_list1 = [num for num in range(1, 101)]
my_list2 = [num*2 for num in range(1, 101)]
my_list3 = [num**2 for num in range(1, 101)]
my_list4 = [num**2 for num in range(1, 101) if num%2==0]

# Set 
my_set = {char for char in 'hello'}
my_set1 = {num for num in range(1, 101)}
my_set2 = {num*2 for num in range(1, 101)}
my_set3 = {num**2 for num in range(1, 101)}
my_set4 = {num**2 for num in range(1, 101) if num%2==0}

# Dictionay
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k:v**2 for k, v in simple_dict.items()}
my_dict2 = {k:v**2 for k, v in simple_dict.items() if v%2==0}
my_dict3 = {num:num*2 for num in [1,2,3,4,5]}


some_list = ['a', 'b', 'c', 'd', 'b', 'd', 'm', 'n', 'n']


duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))


# print(duplicates)

x=1
y=1
z=1

# ans = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]
# print ans
