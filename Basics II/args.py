# *args **kwargs

def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total += items
    print(total)
    return sum(args) + total;

print(super_func(1,2,3,4,5, num1=10, num2=20))

# Walrus Operator
a = 'salimhossain'

if((n := len(a)) > 10):
    print(f'Too long {n} elements')
    
while((n := len(a)) > 2):
    print(n)
    a = a[:-1]