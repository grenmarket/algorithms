board = "CCCCCCCCBBBBBBBBCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC"


def mapToArray(s):
    a = []
    for ch in board:
        # (a,b) a: 0 if white, 1 if black, b: how many times flipped
        a.append((0, 0) if ch == 'B' else (1, 0))
    return a

def flip(i, n):
    a = n[i]
    if a[0] == 1:
        n[i] = (0, a[1] + 1)
    else:
        n[i] = (1, a[1] + 1)

def pretty(n):
    s = ""
    for i in range(0, 64):
        if i % 8 == 0:
            s += "\n"
        s = s + ('B' if n[i][0] == 0 else 'C')
    s += "\n"
    print(s)

def adjacent(k):
    row = (k - 1) // 8
    col = (k - 1) % 8
    adj = set()
    for x in [row - 1, row, row + 1]:
        for y in [col - 1, col, col + 1]:
            if 0 <= x < 8 and 0 <= y < 8:
                adj.add(x * 8 + y)
    adj.remove(k - 1)
    return adj

def move(k, n):
    for coord in adjacent(k):
        flip(coords, n)

def done(n):
    first = n[0][0]
    for i in n:
        if i[0] != first:
            return False
    return True

def fieldpower(i, n):
    field = n[i]
    sum = 0
    for adj in adjacent(i + 1):
        sum += (1 if field[0] == 0 else -1)
    return sum

def fieldflip(i, n):


def rankfields(n):
    return sorted(n, key = lambda t: 

n = mapToArray(board)

