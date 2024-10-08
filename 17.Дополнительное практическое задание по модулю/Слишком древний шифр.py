def f(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
               result += f'{i}{j}'
    return result
n = int(input())
print(f'{n} - {f(n)}')
