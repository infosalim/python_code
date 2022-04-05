# def say_hello(name, emoji):
#     print(f'Hi, I\'m {name} {emoji}')

# say_hello('Salim', ':)')
# say_hello(':)', 'Salim')
# say_hello(emoji=':)', name='Salim')

# # Default Parameters
# def sayHi (name, emo=':)'):
#     print(f'Hi {name} {emo}')

# sayHi('Salim', ':(')
# sayHi('Salim')

def func(a, b):
    '''
    Info: This is Docstring
    '''
    def func_2(a, b):
        return a + b
    return func_2(a, b)


res = func(10,20)
# print(res)
# func()
help(func) # what does the function
print(func.__doc__)