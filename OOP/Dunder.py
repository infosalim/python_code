class Toy():
    def __init__(self, color, age):
        self._color = color
        self._age = age
        self._my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self._color}'

    def __len__(self):
        return 5

    # def __del__(self):
    #     print('deleted!')

    def __call__(self, a, b):
        print(a+b)
    
    def __getitem__(self, i):
        return self._my_dict[i]


action1 = Toy('red', 0)

# print(action1.__str__())
# print(str(action1))
# print(len(action1))
# del(action1)
print(action1(2, 3))
print(action1['name'])

