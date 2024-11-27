def personal_sum(numbers):
    incorrect_data = 0
    sum = 0
    for number in numbers:
        try:
            sum += number
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1
    return (sum, incorrect_data)


def calculate_average(numbers):
    try:
        sum, incorrect_data = personal_sum(numbers)
        return sum / (len(numbers) - incorrect_data)
    except TypeError:
        print('В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0
    

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать