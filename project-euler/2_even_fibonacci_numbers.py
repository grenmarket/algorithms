sumset = set()
curr1 = 1
curr2 = 2
while curr2 <= 4000000:
    if curr1 % 2 == 0:
        sumset.add(curr1)
    if curr2 % 2 == 0:
        sumset.add(curr2)
    c = curr2
    curr2 = curr1 + curr2
    curr1 = c
sum = 0
for n in sumset:
    sum = sum + n
print(sum)

