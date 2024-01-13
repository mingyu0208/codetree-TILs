a,b,c = map(int,input().split())
sat = False

for i in range(a,b+1):
    if c%i==0:
        sat = True

if sat==True:
    print("YES")
else:
    print("NO")