n = int(input())
hap = 0

for i in range(1,101):
    hap+=i
    if hap>=n:
        break
print(i)