n = 5

arr_list = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    arr_list[0][i] = 1
    arr_list[i][0] = 1

for i in range(1, n):
    for j in range(1,n):
        arr_list[i][j] = arr_list[i-1][j] + arr_list[i][j-1]



for elem in arr_list:
    print(*elem)