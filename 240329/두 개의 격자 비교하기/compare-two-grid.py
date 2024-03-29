n,m = map(int,input().split())

arr_1d = [list(map(int,input().split())) for _ in range(m)]
arr_2d = [list(map(int,input().split())) for _ in range(m)]
for i in range(n):
    for j in range(m):
        if arr_1d[i][j] == arr_2d[i][j]:
            arr_1d[i][j] = 0
        else:
            arr_1d[i][j] = 1
    
for i in range(n):
    for j in range(m):
        print(arr_1d[i][j],end=" ")
    print()