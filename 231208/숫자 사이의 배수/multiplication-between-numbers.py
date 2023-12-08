a,b = map(int,input().split())

count = 0
sumi= 0
avg = 0
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        sumi+=i
        count+=1
        avg = sumi/count

print(f'{sumi} {avg:.1f}')