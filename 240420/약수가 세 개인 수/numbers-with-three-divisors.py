import sys
start, end = map(int,sys.stdin.readline().split())
ans = 0


for elem in range(start,end+1):
    sum_val = 0
    for i in range(1,elem+1):
        if elem % i ==0:
            sum_val+=1

    if sum_val == 3:
        ans+=1
print(ans)