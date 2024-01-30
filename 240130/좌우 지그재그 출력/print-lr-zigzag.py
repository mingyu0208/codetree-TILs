n = int(input())

cnt = (n*2)

for i in range(1,n+1):
    for j in range(n):
        if i%2==0:
            print(cnt,end=" ")
            cnt-=1
        else:
            if i==1:
                print(j+1,end=" ")
                
            else:
                print(cnt+n+1,end=" ")
                cnt+=1
    print()