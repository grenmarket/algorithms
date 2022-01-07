factors = [i for i in range(2,21)]

curr = 1
found = False

for i in range(1, 19):
    for j in range(0, i):
        if factors[i] % factors[j] == 0:
            factors[i] = int(factors[i]/factors[j])

for f in factors:
    curr = curr * f

print(curr)
