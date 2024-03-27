n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if arr[i] == 2:
        cnt += 1
        if cnt == 3:
            print(i+1)  # 위치는 1부터 시작하므로 인덱스에 1을 더해 출력합니다.
            break