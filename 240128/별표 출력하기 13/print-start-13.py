n = int(input())

for i in range(n):
    if i%2==0:
        for _ in range(n):
            print("",end=" ")
    else:
        for _ in range(n):
            print("*",end=" ")
    print()