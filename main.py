from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets

Form, Window = uic.loadUiType("GUIsquare.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def square():  # функция решения квадратного уравнения
    a = int(form.input_a.text())
    b = int(form.input_b.text())
    c = int(form.input_c.text())  # запись введенных значений в переменную

    if a == 0:  # блок определения вида уравнения
        form.output1.setText("Нет решений!")
    else:
        if b == 0:  # блок проверки на неполность квадратного урванения
            if -c / a < 0:
                
                equal = str(a) + "x^2+" + str(c) + "=0"  # создание графиского выражения для отображения

                form.output1.setText(equal)  # вывод выражения
                               
                form.output2.setText("Нет решений!")  # вывод ответа
            else:
                if c < 0:  # блок сравнение коэфициента с для правильного отображенич выражения
                    equal = str(a) + "x^2 " + str(c) + "=0"
                else:
                    equal = str(a) + "x^2+" + str(c) + "=0"

                form.output1.setText(equal)  # вывод выражения

                x1 = ((-c / a)) ** .5  # нахождение превого х
                x2 = -x1  # нахождения второго х

                x1 = "x1=" + str(x1)  # преобразование в строку
                x2 = "x2=" + str(x2)

                form.output2.setText(x1)  # вывод значений
                form.output3.setText(x2)
        elif c == 0:
            if b < 0:
                equal = str(a) + "x^2 " + str(b) + "x=0"
            else:
                equal = str(a) + "x^2+" + str(b) + "x=0"
            x1 = "x1=0"
            x2 = -(b / a)

            x2 = "x2=" + str(x2)

            form.output1.setText(equal)
            form.output2.setText(x1)  # вывод значений
            form.output3.setText(x2)
        elif a == 0 and b == 0:
            x = "x1=0"
        else:
            if b < 0 and c < 0:
                equal = str(a) + "x^2 " + str(b) + "x " + str(c) + "=0"
            elif b < 0:
                equal = str(a) + "x^2 " + str(b) + "x+" + str(c) + "=0"
            elif c < 0:
                equal = str(a) + "x^2+" + str(b) + "x " + str(c) + "=0"
            else:
                equal = str(a) + "x^2+" + str(b) + "x+" + str(c) + "=0"
            discriminant = b ** 2 - 4 * a * c
            if discriminant < 0:
                form.output1.setText("Нет решений!(D < 0)")
            elif discriminant == 0:
                x = (-b + discriminant ** .5) / 2 * a
                x = "x=" + str(x)
                discriminant = "D=" + str(discriminant)
                form.output1.setText(equal)
                form.output2.setText(discriminant)
                form.output3.setText(x)
            elif discriminant > 0:
                x1 = (-b + discriminant ** .5) / 2 * a
                x2 = (-b - discriminant ** .5) / 2 * a
                discriminant = "D=" + str(discriminant)
                x1 = "x1=" + str(x1)
                x2 = "x2=" + str(x2)
                form.output1.setText(equal)
                form.output2.setText(discriminant)
                form.output3.setText(x1)
                form.output4.setText(x2)


form.reshat.clicked.connect(square)

app.exec()
