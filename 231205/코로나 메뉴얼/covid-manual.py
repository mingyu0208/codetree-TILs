a,b = input().split()
c,d = input().split()
e,f = input().split()
Ac=0


if (a=='Y' and int(b)>=37):
    Ac+=1
if (c=='Y' and int(d)>=37):
    Ac+=1
if (e=='Y' and int(f)>=37):
    Ac+=1

    

if Ac>=2:
    print("E")
else:
    print("N")