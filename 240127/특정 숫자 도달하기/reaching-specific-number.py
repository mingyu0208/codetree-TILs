arr = list(map(int, input().split()))
sum_v = 0
cnt = 0

for i in arr:
    if i >= 250:
        break
    sum_v+=i
    cnt+=1

avg = sum_v/cnt

print(f'{sum_v} {avg:.1f}')