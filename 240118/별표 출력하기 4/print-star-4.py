n = int(input())

for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

for a in range(1, n):
	for _ in range(a+1):
		print("*", end=" ")
	print()