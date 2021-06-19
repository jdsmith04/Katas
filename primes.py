from math import isqrt

primes = [2]

for integer in range(3, 1000):
    square_root = isqrt(integer)
    primes.append(integer)
    for prime_number in primes:
        if prime_number <= square_root:
            print(f'integer square root: {square_root}')
            print(f'{integer} / {prime_number} = {integer // prime_number} remainder {integer % prime_number}')
            if integer // prime_number > 1 and integer % prime_number == 0:
                print('NOT PRIME\n')
                primes.remove(integer)
                break
            if prime_number == square_root:
                print('PRIME!!!\n')
                break
        else:
            print('PRIME!!!\n')
            break

print(primes)
