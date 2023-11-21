inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])

if a<b and a<c and a>=b and a>=c:
	print(a)
elif b<a and b<c and b<=a and b<=c :
	print(b)
elif c<a and c<b and c<=a and c<=b:
	print(c)