n = int(input())

for i in range(2 * n):
	if i % 2 == 1:
		for _ in range(1 + i // 2):
			print("* ", end="")
	else:
		for _ in range(n - i // 2):
			print("* ", end="")
	print()