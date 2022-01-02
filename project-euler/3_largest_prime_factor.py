def get_div(n, minV):
    div = -1
    for i in range(minV, int(n ** 0.5)):
        if (n % i == 0 and div < 0):
            print("found div: {}".format(i))
            div = i
    return div


def factors(n):
    factors = set()
    curr = n
    currDiv = 2
    while True:
        currDiv = get_div(curr, currDiv)
        if currDiv == -1:
            return factors
        else:
            print(currDiv)
            factors.add(currDiv)
            curr = curr // currDiv

factors(600851475143)
