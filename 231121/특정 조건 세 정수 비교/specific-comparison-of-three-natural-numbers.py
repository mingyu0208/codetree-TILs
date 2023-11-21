inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])
c = int(arr[2])

# 출력
if a <= b and a <= c:
	print("1", end=" ")
else:
	print("0", end=" ")

if a == b and b == c:
	print("1")
else:
	print("0")