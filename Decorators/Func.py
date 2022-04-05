def hello():
    print('hellloooo')
    
greet = hello

del hello

def hello():
    print('hi')

greet2 = hello

print(greet)
print(greet2)
