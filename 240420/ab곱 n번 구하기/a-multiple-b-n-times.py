n = int(input())
answer = []
for i in range(n):
    a,b= map(int,input().split())
    cnt = 1
    for i in range(a,b+1):
        cnt*=i
    
    print(cnt)