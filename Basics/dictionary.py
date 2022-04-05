# Dictionary 

dictionary = {
    'name': 'Salim',
    'age': 23
}
dictionary['profession'] = 'Software Engineer'
print(dictionary)
# .get() dictionary method will check the key is exist or not, second item will be the default value 
print(dictionary.get('position'))
print(dictionary.get('position', 'Software Engineer'))

# creating a new dictionary

user = dict(name='salim')
user2 = user.copy()
user.clear()

print(user)
print(user2)