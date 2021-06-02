primes = [2]

for i in range(3, 100):
    primes.append(i)
    for p in primes:
        print(i, p)
        print(f'division {i // p} remainder {i % p}')
        if i // p > 1 and i % p == 0:
            print('NOT PRIME')
            primes.remove(i)
            break
        if i // p == 1 and i % p == 0:
            print('PRIME')


print(primes)
