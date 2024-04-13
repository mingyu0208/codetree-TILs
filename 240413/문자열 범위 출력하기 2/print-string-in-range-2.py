arr = input()
n = int(input())
len1 = len(arr)
cnt = 0

for i in range(len1 - 1, -1, -1):
	# 주어진 개수만큼 출력했을 경우 for문을 나갑니다.
	if cnt >= a:
		break
	print(string[i], end="")
	cnt += 1