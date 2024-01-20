n = int(input())



for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for a in range( (2 * n) - (2 * i) - 1):
        print("*",end=" ")
    print()