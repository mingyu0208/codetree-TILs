n = int(input())
cnt = "A"

for i in range(n):
    for j in range(n):
        if j >= i:
            print(cnt,end=" ")
            cnt = chr(ord(cnt)+1)
            if cnt > 'Z':
                cnt = 'A'
            
        else:
            print(" ",end=" ")   
    print()