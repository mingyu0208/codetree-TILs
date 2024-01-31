# ord 문자를 => 숫자로 chr 숫자를 => 문자로

n = int(input())
cnt = 'A'
for i in range(1,n+1):
    for j in range(1,i+1):
        print(cnt,end="")
        cnt = chr(ord(cnt)+1)
    print()