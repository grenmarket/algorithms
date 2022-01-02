board = "CCCCCCCCBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"

visited = set()
length = 0

def mapToArray(s):
    a = []
    for ch in board:
        a.append(0 if ch == 'B' else 1)
    return a

def flip(i, n):
    a = n[i]
    if a == 1:
        n[i] = 0
    else:
        n[i] = 1

def pretty(n):
    s = ""
    for i in range(0, 64):
        if i % 8 == 0:
            s += "\n"
        s = s + ('B' if n[i] == 0 else 'C')
    s += "\n"
    print(s)

def adjacent(k):
    row = (k - 1) // 8
    col = (k - 1) % 8
    adj = set()
    for x in [row - 1, row, row + 1]:
        for y in [col - 1, col, col + 1]:
            if 0 <= x < 8 and 0 <= y < 8:
                adj.add((x, y))
    adj.remove((row, col))
    return adj

def move(k, n):
    for coord in adjacent(k):
        i = coord[0] * 8 + coord[1]
        flip(i, n)

def toArrayCoord(coords):
    return coords[0] * 8 + coords[1]

def bestMove(n):
    bestMin = 8
    bMinCo = None
    bestMax = -8
    bMaxCo = None
    for i in range(0, 64):
        adj = adjacent(i+1)
        sum = 0
        for coord in adj:
            sum += (-1 if n[toArrayCoord(coord)] == 0 else 1)
            if sum < bestMin:
                bestMin = sum
                bMinCo = i
            if sum > bestMax:
                bestMax = sum
                bMaxCo = i
    return (bMinCo, bMaxCo)

def done(n):
    first = n[0]
    for i in n:
        if i != first:
            return False
    return True


n = mapToArray(board)

while not done(n):
    b = bestMove(n)
