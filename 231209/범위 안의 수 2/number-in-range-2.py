hap = 0
avg = 0
count = 0



for i in range(10):
    a = int(input())
    if a>=0 and a<=200:
        hap+= a
        count+=1
        avg = hap/count
print(f'{hap} {avg:.1f}')