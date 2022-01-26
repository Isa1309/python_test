class Phone:
    def __init__(self, number, camera, screen, CPU, memory, touch_id, flash):
        if isinstance(number, str):
            self.number = number
        else:
            raise ValueError('Number is not str')
        if isinstance(camera, float):
            self.camera = camera
        else:
            raise Exception('Camera is not float')
        if isinstance(screen, bool):
            self.screen = screen
        else:
            raise Exception('Screen is not bool')
        if isinstance(CPU, float):
            self.cpu = CPU
        else:
            raise Exception('CPU is not float')
        if isinstance(memory, int):
            self.memory = memory
        else:
            raise Exception('Memory is not integer')
        if isinstance(touch_id, bool):
            self.touch_id = touch_id
        else:
            raise Exception('Touch Id is not bool')
        if isinstance(flash, bool):
            self.flash = flash
        else:
            raise ValueError('Flash is not bool')


    def __str__(self):
        return f'Number: {self.number}\n' \
               f'Camera: {self.camera}\n' \
               f'Screen: {self.screen}\n' \
               f'CPU: {self.cpu}\n' \
               f'Memory: {self.memory}\n' \
               f'Touch Id: {self.touch_id}\n' \
               f'Flash: {self.flash}\n'

nokia_6300 = Phone('+996663210', 1.2, False, 0.7, 512, False, True)
print(nokia_6300)

class Iphone(Phone):
    def __init__(self, number, camera, screen, CPU, memory, touch_id, flash, ecosystem, fame, icloud):
        super().__init__(number, camera, screen, CPU, memory, touch_id, flash)
        if isinstance(ecosystem, bool):
            self.eco = ecosystem
        else:
            raise ValueError('Ecosystem is boolean')
        if isinstance(fame, str):
            self.fame = fame
        else:
            raise ValueError('Fame is string')
        if isinstance(icloud, int):
            self.icloud = icloud
        else:
            raise ValueError('Icloud is integer')
    def __str__(self):
        return super(Iphone, self).__str__() + f'Ecosystem: {self.eco}\n' \
                                               f'Fame: {self.fame}\n' \
                                               f'ICloud: {self.icloud}GB\n'

iphone_1 = Iphone('+987654321987', 16.0, True, 2.4, 1024, True, True, True, 'This is Iphone',
                  icloud=32)
print(iphone_1)
