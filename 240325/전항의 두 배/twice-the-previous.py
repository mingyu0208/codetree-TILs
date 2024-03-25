arr = list(map(int, input().split()))
i = 0

while len(arr) != 12: # 이 부분에서 배열의 길이가 왜 12여야 정답이 되는 건가요?
    x = (arr[-2] * 2) + arr[-1]
    arr.append(x)
    print(arr[i], end=" ")
    i += 1