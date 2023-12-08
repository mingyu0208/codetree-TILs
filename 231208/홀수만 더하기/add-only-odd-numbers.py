result = 0


n = int(input())

for i in range(n):
    a= int(input())
    if a%2==1 and a%3==0:
        result+=a

    
    
print(result)