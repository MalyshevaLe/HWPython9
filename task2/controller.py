from model import (division, multiplication, subtraction, addition)
from view import (get_value, show_menu, view_data)

# def button_click():
#     value_a, value_b = get_value()
#     result = addition(value_a, value_b)
#     view_data(result, "result")

def operations():
    
    while True:
        choice = show_menu()
        if choice == 1:
            value_a, value_b = get_value()
            result = (f'{value_a}, {value_b}')
            view_data(result, 'Сохраненные переменные')
        elif choice == 2:
            result = addition(value_a,value_b)
            view_data(result, 'Результат сложения')
        elif choice == 3:
            result = subtraction(value_a,value_b)
            view_data(result, 'Результат вычитания')
        elif choice == 4:
            result = multiplication(value_a,value_b)
            view_data(result, 'Результат умножения')
        elif choice == 5:
            if value_b == 0:
                print('Был введен ноль, на ноль делить я не умею!')
            else:
                result = division(value_a,value_b)
                view_data(result, 'Результат деления')
        elif choice == 6:
            print('\nРаботу закончил, Досвидули!\n')
            break
        else:
            print('\nНеверный выбор, попробуйте еще раз.')