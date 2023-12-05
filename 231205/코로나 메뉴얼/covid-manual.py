count=0
for i in range(3):
    a,b = input().split()
    if a=="Y" and int(b)>=37:
        count+=1
if count>=2:
    print("E")
else:
    print("N")