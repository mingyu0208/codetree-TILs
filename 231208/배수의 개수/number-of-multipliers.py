count3 = 0 
count5= 0

for _ in range(10):
    a = int(input())
    if a%3==0:
        count3+=1
    if a%5==0:
        count5+=1
print(f'{count3} {count5}')