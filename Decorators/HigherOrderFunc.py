def greet(func):
    func()

def greet2():
    def func():
        return 'hi'
    return func

print(greet2())