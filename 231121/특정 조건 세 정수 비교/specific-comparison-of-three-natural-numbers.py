inp = input().split()

a,b,c = int(inp[0]),int(inp[1]),int(inp[2])

# 출력
if a <= b and a <= c:
	print("1", end=" ")
else:
	print("0", end=" ")

if a == b and b == c:
	print("1")
else:
	print("0")