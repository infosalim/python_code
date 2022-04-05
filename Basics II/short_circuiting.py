email = True
password = False

if email and password:
    print('You can login')

if not email or not password:
    print('Wrong credentials')
else:
    print('Login')

print('1' > 'A')