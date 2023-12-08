c ,n = input().split()

if c=='A':
    for i in range(1,int(n)+1,1):
        print(i,end=" ")
else:
    for j in range(int(n),1,-1):
        print(j,end=" ")