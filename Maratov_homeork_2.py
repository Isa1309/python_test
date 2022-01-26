class Elementary_School:
    def __init__(self, maths, russian_language, english_language):
        if isinstance(maths, str):
            self.maths = maths
        else:
            raise ValueError('Math is string')
        if isinstance(russian_language, str):
            self.russian_language = russian_language
        else:
            raise ValueError('Russian language is string')
        if isinstance(english_language, str):
            self.english_language = english_language
        else:
            raise ValueError('English language is string')

    def __str__(self):
        return f'Math: {self.maths}\n' \
               f'Russian language: {self.russian_language}\n' \
               f'English language: {self.english_language}\n'


class_4 = Elementary_School('Умножение и деление трехзначных чисел',
                            'Разбор предложений по главным членам предложения',
                            'Алфавит и счет чисел до 100')
print(class_4)


class Secondary_School(Elementary_School):
    def __init__(self, maths, russian_language, english_language, biology, physics):
        super().__init__(maths, russian_language, english_language)
        if isinstance(biology, str):
            self.biology = biology
        else:
            raise ValueError('Biology is string')
        if isinstance(physics, str):
            self.physics = physics
        else:
            raise ValueError('Physics is string')

    def __str__(self):
        return super(Secondary_School, self).__str__() + f'Biology: {self.biology}\n' \
                                                         f'Physics: {self.physics}\n'


class_7 = Secondary_School('Решение линейных уравнений и построение графиков',
                           'Синтаксический разбор сложного предложения', 'Времена глаголов',
                           'Живые организмы и их тела', 'Закон Архимеда, Ускорение тела')
print(class_7)


class Older_School(Secondary_School):
    def __init__(self, maths, russian_language, english_language, biology,
                 physics, economy, pre_conscription_training):
        super().__init__(maths, russian_language, english_language, biology, physics)
        if isinstance(economy, str):
            self.economy = economy
        else:
            raise ValueError('Economy is string')
        if isinstance(pre_conscription_training, str):
            self.pre_conscription_training = pre_conscription_training
        else:
            raise ValueError('Pre-conscription training is string')

    def __str__(self):
        return super(Older_School, self).__str__() + f'Economy: {self.economy}\n' \
                                                     f'Pre-conscription training: {self.pre_conscription_training}\n'


class_11 = Older_School('Логорифмы, вектора, системы уравнений', 'Виды сложных предложений',
                        'Неличные формы глагола. Инфинитив. Герундий',
                        'Основы экологии. Взаимодействие человека и природы',
                        'Электромагнитная индукция. Колебания и волны',
                        'Экономические цели и функции государства', 'Теоретическое и практическое освоение')
print(class_11)

"""
№1 ЗАДАНИЕ: 1-74 строка
"""


class Windows:
    def __init__(self, password, keyword):
        self._password = password
        self.__keyword = keyword


user = Windows('567831', 'Dog')
print(user)

"""
№2 ЗАДАНИЕ: 81-88 строка
"""


class Engine:
    def __init__(self, title, power, valves_per_cylinder, overclocking):
        self.title = title
        self.power = power
        self.valves_per_cylinder = valves_per_cylinder
        self.overclocking = overclocking

    def __str__(self):
        return f'\nTitle: {self.title}\n' \
               f'Power: {self.power} л.с.\n' \
               f'Valves per cylindr: {self.valves_per_cylinder}'


class HONDA(Engine):
    def speed(self):
        return f'Acceleration time to 100 km/h {self.overclocking} seconds'


class NISSAN(Engine):
    def speed(self):
        return f'Acceleration time to 100 km/h {self.overclocking} seconds\n'


class TOYOTA(Engine):
    def speed(self):
        return f'Acceleration time to 100 km/h {self.overclocking} seconds'


honda_nsx = HONDA('3.5h V6 Turbo', '581', '6', '3')
toyota_supra = TOYOTA('2JZ-GTE', '324', '4', '4,3')
nissan_gtr = NISSAN('VR38DETT', '600', '4', '2,89')
print(honda_nsx)
print(honda_nsx.speed())
print(toyota_supra)
print(toyota_supra.speed())
print(nissan_gtr)
print(nissan_gtr.speed())

"""
№3 ЗАДАНИЕ: 95-131 строка
"""


class The_Property:
    def __init__(self, plot, living_spaces):
        self.plot = plot
        self.living_spaces = living_spaces

    def __str__(self):
        return f'Plot: {self.plot} соток\n' \
               f'Living Spaces: {self.living_spaces} квадратных метров\n'


class House(The_Property):
    def __init__(self, plot, living_spaces, rooms):
        super().__init__(plot, living_spaces)
        self.rooms = rooms

    def __str__(self):
        return super(House, self).__str__() + f'Rooms: {self.rooms} комнат\n'


class Cottage(House):
    def __init__(self, plot, living_spaces, rooms, garage):
        super().__init__(plot, living_spaces, rooms)
        self.garage = garage

    def __str__(self):
        return super(Cottage, self).__str__() + f'Garage: {self.garage} парковочных мест\n'


class Mansion(Cottage):
    def __init__(self, plot, living_spaces, rooms, garage, pool):
        super().__init__(plot, living_spaces, rooms, garage)
        self.pool = pool

    def __str__(self):
        return super(Mansion, self).__str__() + f'Pool: {self.pool} квадратных метров\n'


house = House('3', '120', '5')
cottage = Cottage('10', '280', '8', '2')
mansion = Mansion('50', '1200', '15', '5', '200')
print(house)
print(cottage)
print(mansion)

"""
№4 ЗАДАНИЕ: 138-180 строка
"""
