n = int(input())

if n==1:
    print(31)
elif n==2:
    print(28)
elif n%2==0 and n>=1 and n<=7:
    print(30)
elif n%2==0 and n>=8 :
    print(31)
else:
    print(30)