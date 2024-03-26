A = 0
B = 0
C = 0
D = 0
cnt = 0

for i in range(3):
    a,b = input().split()
    b = int(b)
    
    if a=='Y' and b>=37:
        A+=1
        cnt+=1
    elif a == 'N' and b>=37:
        B+=1
    elif a == 'Y':
        C+=1
    else:
        D+=1


if cnt>=2:
    print(f'{A} {B} {C} {D} E')
else:
    print(f'{A} {B} {C} {D}')