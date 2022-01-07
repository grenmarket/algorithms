primes = [2]
n = 3
while len(primes) < 10001:
    isprime = True
    index = 0
    while isprime and index < len(primes):
        if n % primes[index] != 0:
            index += 1
        else:
            isprime = False
    if isprime:
        primes.append(n)
    n += 1

print(primes[-1])

