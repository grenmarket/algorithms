import sys

def triangle(n):
    if n == 1:
        return [1]
    else:
        prev = triangle(n-1)
        curr = [prev[i] + prev[i+1] for i in range(0, len(prev) - 1)]
        curr.insert(0, prev[0])
        curr.append(prev[-1])
        return curr

def countpaths(n):
    return triangle(n*2+1)[n]


print(countpaths(int(sys.argv[1])))
