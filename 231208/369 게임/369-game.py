n= int(input())



for i in range(1,n+1,1):
    if i%3==0 or i%10 in [3,6,9] or i//10 in [3,6,9]:
        print(0,end=" ")
    else:
        print(i,end=" ")