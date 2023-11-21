inp = input().split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

if a<=b and a<=c:
	print(a)
elif b<=a and b<=c:
	print(b)
else:
	print(c)