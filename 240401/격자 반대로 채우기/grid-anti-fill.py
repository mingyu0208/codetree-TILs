n = int(input())

arr_2d = [ [0 for _ in range(n)] for _ in range(n)]
cnt = 1

for row in range(n):
    if row%2==0:
        for j in range(n-1,-1,-1):
            arr_2d[j][row] = cnt
            cnt += 1
    else:
        for j in range(n):
            arr_2d[j][row] = cnt 
            cnt+=1

for i in range(n):
    print(*arr_2d[i][::-1])