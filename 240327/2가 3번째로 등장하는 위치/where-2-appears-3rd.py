n = int(input())
arr = list(map(int,input().split()))
cnt = arr.count(2)
cnt_2 = 0

for i in range(n):
    if cnt_2 <3:
        if arr[i] != 2:
            cnt-=1
            cnt_2+=1
    else:
        break
print(cnt+1)