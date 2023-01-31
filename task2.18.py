A = int(input())
bigest = 0
big = 0
while A != 0:
    if A >= bigest:
        big = bigest
        bigest = A
    elif A >= big:
        big = A
    A = int(input())
print(big)
