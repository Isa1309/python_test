print('\nЗАДАНИЕ №1')


class Project:
    def __init__(self, term, price, backend, frontend, additional_info):
        if isinstance(term, str):
            self.term = term
        else:
            raise ValueError('Term is string')
        if isinstance(price, int):
            self.price = price
        else:
            raise ValueError('Price is integer')
        if isinstance(backend, str):
            self.backend = backend
        else:
            raise ValueError('Backend Objectives is string')
        if isinstance(frontend, str):
            self.frontend = frontend
        else:
            raise ValueError('Frontend Objectives is string')
        if isinstance(additional_info, str):
            self.additional_info = additional_info
        else:
            raise ValueError('Additional Info is string')

    def __str__(self):
        return f'\nTerm: {self.term}\n' \
               f'Price: {self.price}$\n' \
               f'Backend developer tasks: {self.backend}\n' \
               f'Frontend developer tasks: {self.frontend}\n' \
               f'Additional Info: {self.additional_info}'


project_1 = Project('3 months', 5000,
                    'Work with databases', 'Website layout',
                    'Customer from america')
print(project_1)


class Backend(Project):
    def __init__(self, term, price, backend, frontend, additional_info):
        super().__init__(term, price, backend, frontend, additional_info)

    def exp(self, experience):
        return f'Experience in this field: {experience} year'

    def __str__(self):
        return super(Backend, self).__str__()


project_2 = Backend('1.5 months', 2500, 'Work with databases',
                          'Website layout', 'Сomplete in no more than 2 months')
print(project_2)
print(project_2.exp(3))


class Frontend(Project):
    def __init__(self, term, price, backend, frontend, additional_info):
        super().__init__(term, price, backend, frontend, additional_info)

    def status(self, status):
        return f'Developer status: {status}'

    def __str__(self):
        return super(Frontend, self).__str__()


project_3 = Frontend('2 months', 2500, 'Work with databases',
                          'Website layout', 'Сomplete in no more than 2.5 months')
print(project_3)
print(project_3.status('Middle'))


class Full_stack(Backend, Frontend):
    def __init__(self, term, price, backend, frontend, additional_info):
        super().__init__(term, price, backend, frontend, additional_info)

    def __str__(self):
        return super(Full_stack, self).__str__()


project_4 = Full_stack('3 months', 5000, 'Work with databases',
                          'Website layout', 'Сomplete in no more than 3.5 months')
print(project_4)
print(project_4.exp(4))
print(project_4.status('Middle'))
"""
ЗАДАНИЕ №1: 4-87 строка
"""
print('\nЗАДАНИЕ №2')


class examps:
    def __init__(self, physics, math, russian_language, chemistry):
        if isinstance(physics, int):
            self.physics = physics
        else:
            raise ValueError('Physics is integer')
        if isinstance(math, int):
            self.math = math
        else:
            raise ValueError('Math is integer')
        if isinstance(russian_language, int):
            self.russian_language = russian_language
        else:
            raise ValueError('Russian language is integer')
        if isinstance(chemistry, int):
            self.chemistry = chemistry
        else:
            raise ValueError('Chemistry is integer')

    def __str__(self):
        return f'\nGPA in Physics: {self.physics}\n' \
               f'GPA in Math: {self.math}\n' \
               f'GPA in Russian language: {self.russian_language}\n' \
               f'GPA in Chemistry: {self.chemistry}'


max_points = examps(100, 100, 100, 100)
print(max_points)


class School_24(examps):
    def __init__(self, physics, math, russian_language, chemistry):
        super().__init__(physics, math, russian_language, chemistry)

    def add(self):
        i = self.physics + self.math + self.chemistry + self.russian_language
        return f'Total GPA points: {i}'

    def division(self):
        a = (self.physics + self.math + self.chemistry + self.russian_language) / 4
        return f'The average meaning: {a}'

    def __str__(self):
        return super(School_24, self).__str__()


points_school24 = School_24(76, 80, 72, 65)
print(points_school24)
print(points_school24.add())
print(points_school24.division())


class School_61(examps):
    def __init__(self, physics, math, russian_language, chemistry):
        super().__init__(physics, math, russian_language, chemistry)

    def  add(self):
        i = self.physics + self.math + self.chemistry + self.russian_language
        return f'Total GPA points: {i}'

    def division(self):
        a = (self.physics + self.math + self.chemistry + self.russian_language) / 4
        return f'Academic performance: {a} %'

    def __str__(self):
        return super(School_61, self).__str__()


points_school61 = School_61(80, 90, 75, 70)
print(points_school61)
print(points_school61.add())
print(points_school61.division())


class School_70(examps):
    def __init__(self, physics, math, russian_language, chemistry):
        super().__init__(physics, math, russian_language, chemistry)

    def add(self):
        i = (self.physics + self.math) / 2
        return f'Academic performance physics and math: {i} %'

    def division(self):
        a = (self.chemistry + self.russian_language) / 2
        return f'Academic performance humanities: {a} %'

    def __str__(self):
        return super(School_70, self).__str__()


points_school70 = School_70(60, 70, 80, 55)
print(points_school70)
print(points_school70.add())
print(points_school70.division())
"""
ЗАДАНИЕ №2: 94-187 строка
"""
print('\nЗАДАНИЕ №3')


class Cinema:
    def __init__(self, film_1, price_1, film_2, price_2, film_3, price_3, film_4, price_4):
        self.film_1 = film_1
        self.price_1 = price_1
        self.film_2 = film_2
        self.price_2 = price_2
        self.film_3 = film_3
        self.price_3 = price_3
        self.film_4 = film_4
        self.price_4 = price_4

    def __str__(self):
        return f'\nСтоимость "{self.film_1}" - {self.price_1} сом\n' \
               f'Стоимость "{self.film_2}" - {self.price_2} сом\n' \
               f'Стоимость "{self.film_3}" - {self.price_3} сом\n' \
               f'Стоимость "{self.film_4}" - {self.price_4} сом\n' \



cinema = Cinema('Форсаж 7', 220, 'Человек-паук: Нет пути домой', 300,
                'Астрал 4', 200, 'Матрица: Воскрешение', 240)
print(cinema)


# class Starbucks:
#     def __init__(self, name_1, name_2, name_3, name_4):
#         self.name_1 = name_1
#         self.name_2 = name_2
#         self.name_3 = name_3
#         self.name_4 = name_4
#
#     def __len__(self, name_1):
#         if len(name_1) >= 9:
#             return f'{(end, 0)}'
#         elif 5 <= len(name_1) < 9:
#             return f'{self.name_1}'
#         else:
#             return f'{self.name_1[:]}'
#
#
# client = Starbucks('Addled', 'dogsbody', 'fabled', 'badged')
# print(client)