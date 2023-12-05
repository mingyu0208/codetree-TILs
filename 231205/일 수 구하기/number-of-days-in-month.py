n = int(input())

if n%2==0:
    if n==2:
        print(28)
    else:
        print(30)
else:
    if n%2==0 and n>=8:
        print(31)
    else:
        print(30)