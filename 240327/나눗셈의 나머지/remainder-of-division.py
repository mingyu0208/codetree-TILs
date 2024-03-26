a,b = map(int,input().split())
cnt = [0] * 10
while a > 1:
    cnt[a%b] += 1
    a = a // b

cnt = [elem ** 2 for elem in cnt]
print(sum(cnt))