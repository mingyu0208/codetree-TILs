start, end = map(int,input().split())
ans = 0

for elem in range(start,end+1):
    sum_val = 0
    for i in range(1,elem):
        if elem % i == 0:
            sum_val+= i

    if sum_val == elem:
        ans+=1
print(ans)