arr = list(map(int,input().split()))
count_arr = [0] * 10 

for elem in arr:
	if elem == 0:
		break
	if elem < 10:
		continue
	count_arr[elem // 10] += 1
	
# 1부터 9까지 나온 횟수를 출력
for i in range(1, 10):
	print(f"{i} - {count_arr[i]}")