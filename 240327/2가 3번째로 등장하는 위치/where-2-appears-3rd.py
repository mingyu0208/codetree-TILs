n = int(input())
arr = list(map(int,input().split()))
cnt = 0
for a,b in enumerate(arr):
    while cnt<3:
        if b == 2:
            cnt+=1
    
if cnt==3:
    print(cnt)