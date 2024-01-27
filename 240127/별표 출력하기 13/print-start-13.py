n = int(input())
for i in range(1, n+1):
    if i % 2 == 0:
        print('* '*plus)
        plus += 1
    else:
        print('* '*minus)
        minus -= 1

plus = (n//2 + 1)
minus = n//2

if n % 2 == 0:
    for j in range(1, n +1):
        if j % 2 == 0:
            print('* '*plus )
            plus += 1
        else:
            print('* '*minus)
            minus-= 1
else:
    for k in range(1, n+1):
        if k % 2 == 0:
            print('* '*minus)
            minus -= 1
        else:
            print('* '*plus)
            plus += 1