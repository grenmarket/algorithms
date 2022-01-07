def next(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def length(n, visited):
    length = 1
    curr = n
    while curr != 1:
        visited.add(curr)
        curr = next(curr)
        length += 1
    return length

visited = set()
max = 1
res = 0

for i in range(2, 1000000):
    if i % 10000 == 0:
        print(str(i // 10000) + "%")
    if i not in visited:
        a = length(i, visited)
        if a > max:
            max = a
            res = i

print(max, res)
