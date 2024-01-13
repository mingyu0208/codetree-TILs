a,b = map(int,input().split())

sat = False

for i in range(1,a+1):
    if a%i==0 and b%i==0:
        sat=True


if sat == True:
    print(1)
else:
    print(0)