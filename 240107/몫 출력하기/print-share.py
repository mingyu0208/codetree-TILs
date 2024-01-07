cnt = 0

while True:
    n = int(input())
    cnt+=1
    if n%2==0:
        print(n//2)
        if cnt>3:
            break