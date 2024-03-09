n = list(map(int,input().split()))
sum_val = 0
cnt = 0
avg_1 = 0


for i in n:
    if i==0:
        break
    sum_val+=i
    cnt+=1
    

avg_1 = sum_val/cnt
print(f'{sum_val} {avg_1:.1f}')