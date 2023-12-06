a,b,c = map(int,input().split())

if a>=b and a>=c and b>=c:
    print(b)
    
if b>=a and b>=c and a>=c:
    print(a)

if c>=a and c>=b and a>=b:
    print(a)