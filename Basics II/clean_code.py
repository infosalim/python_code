# bad code
def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False

# good code 
def is_even_good(num):
    if num % 2 == 0:
        return True
    else:
        return False
# better code 
def is_even_better(num):
    if num % 2 == 0:
        return True
    return False
# best code 
def is_even_best(num):
    return num % 2 == 0

print(is_even(10))
print(is_even_good(11))
print(is_even_better(12))
print(is_even_best(13))

