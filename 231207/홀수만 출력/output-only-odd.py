a,b = map(int,input().split())

for i in range(a,b+1,a+1):
    if a%2==1:
        print(i, end=" ")