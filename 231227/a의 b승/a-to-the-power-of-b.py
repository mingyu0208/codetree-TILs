a,b = map(int,input().split())
answer=1

for _ in range(b):
    answer*=a

print(answer)