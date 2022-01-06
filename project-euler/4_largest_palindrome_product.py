max = 0
numbers = (0,0)

for n in range(900,1000):
    for m in range(n, 1000):
        number = n * m
        if (str(number) == str(number)[::-1]):
                if (number > max):
                    max = number
                    numbers = (n,m)
print(max, numbers)
