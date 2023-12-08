n = int(input())

Cls_2 = 0
Lug_3 = 0
Btrm_12 = 0

for i in range(1, n+1):
    if i%12==0:
        Btrm_12+=1

    elif i%3==0:
        Lug_3+=1
        if Lug_3==Btrm_12:
            Lug_3-=1

    elif i%2==0:
        Cls_2+=1
        if Cls_2==Lug_3:
            Cls_2-=1
        

print(Cls_2, Lug_3, Btrm_12)