
# while True:
#     try:
#         age = int(input('Enter your age: '))
#         10/age
#         # raise ValueError('hey cut it out')  --- it through in except bloc
#     except ValueError:
#         print('Please enter a number')
#     except ZeroDivisionError:
#         print('Please enter a number higher than zero')
#     else:
#         print('Thank you')
#         break
    
def sumOfTwo(num1, num2):
    try:
        return num1+num2
    except (TypeError, ZeroDivisionError) as err:
        print(f'ERROR: {err}')
    else:
        pass
    finally:
        pass
    
print(sumOfTwo(1,'2'))