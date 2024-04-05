n,m = map(int,input().split())

arr_2d = [[0 for _ in range(10)]for _ in range(10)]

for i in range(m):
    r,c = tuple(map(int,input().split()))
    arr_2d[r][c] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        print(arr_2d[i][j],end=" ")
    print()