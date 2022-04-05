class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def fun(self):
        print(self.name)
    
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1+ num2
    
    def speak(self):
        print(f'My name is {self._name} and I\'am {self._age} years old!!!')

player = PlayerCharacter('Milas Hossain', 23)
player2 = PlayerCharacter.adding_things(2,4)
player.fun()
print(player2.age)
print(player.speak())