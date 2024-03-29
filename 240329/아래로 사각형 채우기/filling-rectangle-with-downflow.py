n = int(input())
cnt = 1
arr_2d =[ [0 for _ in range(n)] for _ in range(n) ]

for i in range(n):
    for j in range(n):
        arr_2d[j][i] = cnt
        cnt+=1

for elem in arr_2d:
    print(*elem)
# for elem in arr_2d: