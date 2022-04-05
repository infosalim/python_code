
import email


def my_decorator(func):
    def wrap_func(*args,**kwargs):
        func(*args,**kwargs)
    return wrap_func

# @my_decorator
# def hello():
#     print('hellooo')

# @my_decorator
# def ya():
#     print('yaaaaa')

# hello2 = my_decorator(hello)
# ya2 = my_decorator(ya)

# ya2()
# my_decorator(hello)()

@my_decorator
def hithere(sayhi, emoji=':('):
    print(sayhi,emoji)
    
hithere('Hi there')