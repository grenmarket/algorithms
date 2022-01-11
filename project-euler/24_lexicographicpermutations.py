import math
import sys

def p(nth, maxN):
    A = []
    S = [i for i in range(0, maxN + 1)]
    n = nth - 1
    while (n != 0):
        fac = math.factorial(len(S)-1)
        div = math.floor(n/fac)
        A.append(S[div])
        n -= (div * fac)
        S = S[0:div] + S[div+1:]
    A += S
    return A

print(p(int(sys.argv[1]), int(sys.argv[2])))


