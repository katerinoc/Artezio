"""task 2"""


class Student:

    """Constructor"""
    def __init__(self, name):

        self.conf = {'exam_max': 30, 'lab_max': 7, 'lab_num': 10, 'k': 0.61}
        self.name = name
        self.exam_max = 30
        self.lab_max = 7
        self.lab_num = 10
        self.k = 0.61
        self.LABS_DICT = {}
        print(self.conf)

    def make_lab(self, m, n):

        self.LABS_DICT[n] = m
        total = 0
        for item in self.LABS_DICT.values():
            if item <= 7:
                total = total + item
        print(self.LABS_DICT)
        return total

    def make_exam(self, m):

        if m > 30 or m < 0:
             self.LABS_DICT['exam'] = 0
        else:
             self.LABS_DICT['exam'] = m

    def is_certified(self):

        if sum(self.LABS_DICT.values()) >= self.conf['k'] * 100:
            print(sum(self.LABS_DICT.values()), True)
        else:
            print(sum(self.LABS_DICT.values()), False)


ST = Student("Kate")

while 1:
    print('Выберите действие: ')
    print('1. Заполнить данные по практическим заданиям')
    print('2. Заполнить данные по экзамену')
    print('3. Узнать состояние сертификата')
    print('4. Выход')

    RES = int(input())
    if (RES <= 4) and RES > 0:

        if RES == 1:
            print("Введите оценку и номер задания")
            ST.make_lab(float(input()), int(input()))

        if RES == 2:

            print("Введите оценку за экзамен")
            ST.make_exam(float(input()))

        if RES == 3:
            ST.is_certified()
        if RES == 4:
            break

    else:
        print('Ошибка: выберите вариант из списка доступных')
