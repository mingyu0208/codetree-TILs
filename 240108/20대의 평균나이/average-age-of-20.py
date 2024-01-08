sumli = 0
cnt = 0
while True :
    age = int(input())
    if age >19 and age<30:
        sumli+=age
        cnt+=1
        continue
    break
a = sumli/cnt
print(f'{a:.2f}')