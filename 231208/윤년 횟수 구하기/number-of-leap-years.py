n = int(input())
count=0

for i in range(1, n+1):
    if i%400==0  or (i%100!=0 and i%4==0):
        count+=1
print(count)