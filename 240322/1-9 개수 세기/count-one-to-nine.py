n = int(input())
arr = list(map(int,input().split()))

for i in range(1,10):
    cnt = 0
    for elem in arr:
        if i==elem:
            cnt+=1
    print(cnt)