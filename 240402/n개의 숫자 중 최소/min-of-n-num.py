n = int(input())
arr = list(map(int,input().split()))
cnt = 0
for elem in arr:
    if n > elem:
        n = elem
        cnt +=1
print(n,cnt)