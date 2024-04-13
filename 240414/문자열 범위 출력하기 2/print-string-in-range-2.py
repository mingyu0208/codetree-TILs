arr = input()
n = int(input())
cnt = 0

for i in range(len(arr)- 1, -1, -1):
	# 주어진 개수만큼 출력했을 경우 for문을 나갑니다.
	if cnt >= n:
		break
	print(arr[i], end="")
	cnt += 1