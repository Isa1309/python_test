class Animal:
    def __init__(self, kind, max_age, speed):
        if isinstance(kind, str):
            self.kind = kind
        else:
            raise ValueError('Kind is not str')
        if isinstance(max_age, int):
            self.max_age = max_age
        else:
            raise Exception('Max age is not integer')
        if isinstance(speed, int):
            self.speed = speed
        else:
            raise Exception('Speed is not integer')

    def __str__(self):
        return f'Kind: {self.kind}\n' \
               f'Max age: {self.max_age} лет\n' \
               f'Speed: {self.speed} км/ч\n'


cheetah = Animal('predator', 20, 93)
print(cheetah)


class Mammals(Animal):
    def __init__(self, kind, max_age, speed, habitat, childbirth):
        super().__init__(kind, max_age, speed)
        if isinstance(habitat, str):
            self.habitat = habitat
        else:
            raise ValueError('Habitat is str')
        if isinstance(childbirth, str):
            self.childbirth = childbirth
        else:
            raise ValueError('Childbirth is string')

    def __str__(self):
        return super(Mammals, self).__str__() + f'Habitat: {self.habitat}\n' \
                                               f'Prefnancy: {self.childbirth}\n'


blue_whale = Mammals('cetaceans', 37, 85, 'aquatic habitat', 'oviparous')
print(blue_whale)
