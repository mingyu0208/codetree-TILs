n = int(input())

if n%2==0 and n<8:
    if n==2:
        print(28)
    else:
        print(30)
elif n>=8 and n%2==0:
    print(30)
else:
    print(31)