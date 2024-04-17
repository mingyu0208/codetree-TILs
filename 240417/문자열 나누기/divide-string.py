str_all = ""

# n을 입력받습니다.
n = int(input())

# 공백 단위로 문자열을 입력받습니다.
string = input().split()

# 문자열을 전부 붙입니다.
for i in range(n):
	str_all += string[i]
	
# 합쳐진 문자열의 길이를 구합니다.
leng = len(str_all)

# 합쳐진 문자열을 5개의 숫자마다 개행을 하여 출력합니다.
for i in range(leng):
	print(str_all[i], end="")
	if (i + 1) % 5 == 0:
		print()