n = int(input())
arr = list(map(int,input().split()))


cnt = 0
for i in range(n):
	if arr[i] == 2:
		cnt += 1
		
	# 2가 3번째로 등장할 때 그 위치를 출력합니다.
	if cnt == 3:
		print(i + 1)
		break