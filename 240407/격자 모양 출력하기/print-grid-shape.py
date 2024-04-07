n,m = map(int,input().split())

arr_2d = [[0 for _ in range(11)]for _ in range(11)]

cnt = 1

for i in range(m):
    r,c = tuple(map(int,input().split()))
    cnt = r*c
    arr_2d[r][c] = cnt
    

for i in range(1,n+1):
    for j in range(1,n+1):
        print(arr_2d[i][j],end=" ")
    print()