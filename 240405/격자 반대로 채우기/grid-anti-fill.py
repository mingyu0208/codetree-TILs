# a = int(input())
# reg = a**2
# nums = []
# answer = []
# cnt = 1
# for i in range(a):
#     nums.append(cnt)
#     cnt = cnt + 2

# for i in range(1,a+1):
#     an = [0 for _ in range(a)]
#     an[0] =  reg-(a-i)
#     an[1] = (reg-(a-i))-nums[i-1]
#     an[2] = ((reg-(a-i))-nums[i-1])-nums[4-i]
#     an[3] = (((reg-(a-i))-nums[i-1])-nums[4-i])-nums[i-1]
#     answer.append(an)
# print(answer)


n = int(input())
sort = 0
if n%2 == 0:
    sort = 1
else:
    sort = 0

arr_2d = [[0 for _ in range(n)] for _ in range(n)]
cnt_x = n-1
cnt = 1
while cnt_x!=(-1):
    cnt_y = n-1
    if sort == 1:
        if cnt_x%2 == 1:
            for i in range(cnt_y+1):
                arr_2d[cnt_y][cnt_x] = cnt
                cnt += 1
                cnt_y -= 1
        else:
            for i in range(cnt_y+1):
                arr_2d[i][cnt_x] = cnt
                cnt += 1
    else:
        if cnt_x%2 == 0:
            for i in range(cnt_y+1):
                arr_2d[cnt_y][cnt_x] = cnt
                cnt += 1
                cnt_y -= 1
        else:
            for i in range(cnt_y+1):
                arr_2d[i][cnt_x] = cnt
                cnt += 1
    cnt_x -= 1
for i in arr_2d:
    for j in i:
        print(j,end=" ")
    print()
        


# for i in range(n):
#     for j in range(n):
#         arr_2d[i][j]  = cnt 
#         cnt+=1

# for elem in arr_2d:
#     print(elem)