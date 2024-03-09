arr  = list(map(int,input().split()))
cnt = -1
sum_val = 0

for i in arr:
        if i%2==0:
            sum_val+=i
            cnt+=1
    
print(f'{cnt} {sum_val}')