n, m = tuple(map(int, input().split()))
arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 1
for i in range(n):
    for j in range(m):
        arr_2d[i][j] = num
        num += 1

for sub_arr in arr_2d:
    print(*sub_arr)