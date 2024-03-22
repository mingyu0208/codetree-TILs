arr = list(map(int,input().split()))

new_list = []

for i in arr:
    if i==0:
        break
    elif i%2==1:    
        new_list.append(i+3)
    else:    
        new_list.append(i//2)
    
        
print(*new_list)