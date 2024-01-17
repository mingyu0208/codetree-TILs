n = int(input())

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for a in range(j):
    for b in range(j-a):
        print("*",end=" ")
    print()