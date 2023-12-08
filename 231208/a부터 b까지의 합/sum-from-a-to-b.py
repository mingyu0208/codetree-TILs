a,b = map(int,input().split())
result = 0

for i in range(a,b+1,1):
    result+=i
print(result)