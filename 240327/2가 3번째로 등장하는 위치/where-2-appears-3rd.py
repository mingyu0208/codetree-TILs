n = int(input())
arr = list(map(int,input().split()))
lis_val =[]
cnt = 1

for i in range(n):
    
    if arr[i] == 2 and cnt<3:
        cnt+=1
    else:
        continue

print(cnt)