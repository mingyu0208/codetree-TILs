n = int(input())
count=0

for i in range(1, n):
    if i%4==0 and i!=400:
        count+=1
print(count)