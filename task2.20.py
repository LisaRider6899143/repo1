x = int(input())
y = int(input())
i = 1
ans = 1
while y != 0:
    if x != y:
        x = y
        y = int(input())
    while x == y:
        i += 1
        y = int(input())
    if i > ans:
        ans = i
    i = 1
print(ans)
