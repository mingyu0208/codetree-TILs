n = int(input())
cnt = 'A'

for _ in range(1,n+1):
    for _ in range(1,n+1):
        print(cnt,end="")
        cnt = chr(ord(cnt)+1)
    print()