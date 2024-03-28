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

lst =[list(map(int, input().split())) for i in range(4)]
ssum=0
for j, i in enumerate(lst, start=1):
    ssum += sum(i[ :j])
    
    
print(ssum)