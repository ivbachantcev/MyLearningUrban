numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for x in numbers:
    for i in range(2, int(x**.5) + 1):
        if x == 1:
            continue
        if not x % i:
            not_primes.append(x)
            break
    else:
        primes.append(x)
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')
