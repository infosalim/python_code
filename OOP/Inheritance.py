class User():
    def __init__(self, email):
        self._email = email
        
    
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email)
        self._name = name
        self._power = power

    def attact(self):
        print(f'{self._name} is attacking with power {self._power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self._name = name
        self._num_arrows = num_arrows

    def check_arrows(self):
        print(f'{self._name} is attacking with arrows {self._num_arrows}')

    def run(self):
        print('ran really fast')

archer1 = Archer('Anik', 300, 'intofaisal@gmail.com')
wizard1 = Wizard('Salim', 100, 'salimh5757@gmail.com')

# print(wizard1.attact())
# print(wizard1.sign_in())
# print(isinstance(wizard1, User))
# print(wizard1._email)
# print(archer1._email)

    
# introspection
# print(dir(wizard1))


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows, email):
        Wizard.__init__(self, name, power, email)
        Archer.__init__(self, name, arrows, email)
        

hybridborg1 = HybridBorg('Milas', 50, 'milassss', 'assss')

print(hybridborg1.run())
print(hybridborg1.attact())
print(hybridborg1.check_arrows())
print(hybridborg1._email)
print(hybridborg1.sign_in())