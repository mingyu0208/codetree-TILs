n,m = list(map(int,input().split()))

arr_d2 = [
    [0 for i in range(m)]
    for j in range(n)
]
cnt = 1

for i in range(n):
    for j in range(m):
        arr_d2[i][j] = cnt 
        cnt+=1

for i in arr_d2:
    for j in i:
        print(j,end=" ")
    print()