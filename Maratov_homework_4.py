class TimeDesk:
    def __init__(self, seconds):
        self.seconds = int(seconds)
        if self.seconds < 0:
            print('Вы ввели отрицательное число!')

    def day(self):
        i = self.seconds // 86400
        if i >= 1:
            return f'{int(i)} день,'
        else:
            return f'0 день,'

    def hour(self):
        i = self.seconds / 3600
        if 0 < i < 24:
            return f'{int(i)} часов,'
        elif i > 24:
            k = i - (i // 24 * 24)
            return f'{int(k)} часов,'
        else:
            return f'0 часов,'

    def minute(self):
        i = (self.seconds / 60)
        if 0 < i < 60:
            return f'{int(i)} минут,'
        elif i > 60:
            k = i - (i // 60 * 60)
            return f'{int(k)} минут,'
        else:
            return f'0 минут,'

    def second(self):
        i = self.seconds
        if 0 < i < 60:
            return f'{int(i)} секунда'
        elif i > 60:
            k = i - (i // 60 * 60)
            return f'{int(k)} секунда'
        else:
            return f'0 секунда'


sec = TimeDesk(input('Введите количество секунд: '))
print(sec.day(), sec.hour(), sec.minute(), sec.second())

