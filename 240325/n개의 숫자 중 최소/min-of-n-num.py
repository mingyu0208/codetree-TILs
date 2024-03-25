a = int(input())
arr = list(map(int,input().split()))

min_val = arr[0]
cnt = 1

for i in arr:
    if min_val > i:
        min_val = i
        cnt+=1
        

print(f'{min_val} {cnt}')