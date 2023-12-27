n = int(input())
abc = 0

for i in range(1,n):
    if n%i==0:
        abc+=i

if n==abc:
    print('P')
else:
    print('N')