# 변수 선언 및 입력
n = int(input())

# n회 반복합니다.
for _ in range(n):
        inp = input()
        arr = inp.split()

        a = int(arr[0])
        b = int(arr[1])
        lala = 1

        for i in range(a,b+1):
            lala *=i

        print(lala)