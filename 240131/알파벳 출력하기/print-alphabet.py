# ord 문자를 => 숫자로 chr 숫자를 => 문자로

n = int(input())
cnt = 'A'
for i in range(n):
    for j in range(i+1):
        print(cnt,end="")
        cnt = chr(ord(cnt)+1)
        if ord(cnt)> ord('Z'):
            cnt = "A"      
    print()