cnt  =0
n,m = map(int,input().split())

arr = list(map(int,input().split()))

for i in range(n):
    if m == arr[i]:
        cnt+=1
print(cnt)