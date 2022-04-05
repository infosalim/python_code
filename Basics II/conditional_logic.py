is_old = True
is_licenced = True

if not is_old:
    print('you are old enough to drive')
elif is_old and is_licenced:
    print('You are Genious')
else:
    print('you can\'t drive man')

print('You learned conditional logic Dear Salim')

# Ternary Operator

is_authenticated = False

print('You are allowed' if is_authenticated else 'You are not allowed')

print('\n\n\n...\n\n\n')
# Logical Operators
is_magician = True
is_expert = True

if is_magician and is_expert:
    print('Your are a master mafician' )
elif is_magician and not is_expert:
    print('at least you\'re getting there')

if not is_magician:
    print('You need magic powers') 

print('\n\n\n...\n\n\n')

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])