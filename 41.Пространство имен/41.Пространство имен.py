def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

# inner_function() при вызове будет ошибка, т.к. в глобальной области видимости нет этой функции
test_function()