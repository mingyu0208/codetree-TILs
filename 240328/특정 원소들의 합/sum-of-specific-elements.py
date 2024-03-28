# cnt  = 0

# sum_val = [] 
# for i in range(4):
#     arr = list(map(int,input().split()))
#     for j in range(4):
#         sum_val = arr[j]
#         print(sum_val, end= " ")
#     print()

# # for i in :
# #     print(,end=" ")


arr_2d = [
    list(map(int, input().split()))
    for i in range(4)
]
sum_val = 0
	
for i in range(4):
    for j in range(i+1):
        sum_val+= arr_2d[i][j]
print(sum_val)