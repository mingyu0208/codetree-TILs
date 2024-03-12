# 학생 수 n 입력받기
n = int(input())

# 통과한 사람의 수를 나타내는 변수 : pass_people
pass_people = 0

for _ in range(n):
	# 배열에 주어진 수를 입력받아 저장합니다.
	arr = list(map(int, input().split()))
	
	# 4과목의 점수의 합을 구합니다.
	sum_val = sum(arr)
	
	# 평균을 구합니다.
	avg = sum_val / 4
	
	# 출력
	if avg >= 60:
		print("pass")
		pass_people += 1
	else:
		print("fail")

# 통과한 사람의 수 출력
print(pass_people)