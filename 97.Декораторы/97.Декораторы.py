def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        i = 2
        while i * i <= result and result % i != 0:
            i += 1
        if i * i > result:
            print(f'Число {result} является простым')
        else:
            print(f'Число {result} не является простым')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)