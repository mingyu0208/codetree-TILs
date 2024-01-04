n = int(input())
cnt = 0
answer = 0

for i in range(1,n+1):
    answer = n//i
    if answer//i>1:
        cnt+=1
    else:
        break
print(cnt)