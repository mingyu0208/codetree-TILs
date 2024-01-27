# 과목의 개수 n을 입력받습니다.
n = int(input())

# 배열을 구현하여 주어진 수를 입력받습니다.
arr = list(map(float, input().split()))
	
# 배열에 있는 실수들의 합을 구합니다.
sum_val = sum(arr)

#평균 구하기
avg = sum_val / n

# 출력
print(f"{avg:.1f}")

if avg >= 4.0:
	print("Perfect")
elif avg >= 3.0:
	print("Good")
else:
	print("Poor")