a,b,c = map(int,input().split())




# 프린트 a
if (b>=a and b>=c) and a>=c :
    print(a)


if (c>=a and c>=b) and a>=b:
    print(a)


# 프린트 b
if (a>=b and a>=c) and b>=c:
    print(b)


if (c>=a and c>=b) and b>=a :
    print(b)


#프린트 c
if (a>=b and a>=c) and c>=b:
    print(c)


if (b>=a and b>=c) and c>=a:
    print(c)