arr  = list(map(int,input().split()))
cnt = 0
sum_val = 0

for i in arr:
    if i==0:
        break
    if i%2==0:
        cnt+=1
        sum_val+=i
        
    
print(f'{cnt} {sum_val}')