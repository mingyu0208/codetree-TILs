n,m = map(int,input().split())

arr_2d = [ [0 for _ in range(m)] for _ in range(n)]

cnt = 0
for i in  range(m):
    if i%2==0:
        for row in range(n):
            arr_2d[row][i] = cnt 
            cnt+=1
    else:
        for row in range(n-1, -1,-1):
            arr_2d[row][i] = cnt
            cnt+=1

for elem in arr_2d:
    print(*elem)