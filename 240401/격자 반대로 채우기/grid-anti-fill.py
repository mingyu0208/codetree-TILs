n = int(input())

arr_2d = [[0 for _ in range(n)]for _ in range(n)]
cnt = 1

# for i in range(n):
#     for j in range(n): 
#         arr_2d[j][i] = cnt
#         cnt+=1
for i in range(n-1,-1,-1):
    if i%2==0:
        
            for j in range(n):
                arr_2d[j][i] = cnt
                cnt+=1
    else:
        # for revers in range(n):
        for j in range(n-1,-1,-1):
                arr_2d[j][i] = cnt
                cnt+=1
            

for elem in arr_2d:
    print(*elem)