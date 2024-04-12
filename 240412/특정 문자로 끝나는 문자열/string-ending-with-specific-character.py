arr = [
    input()
    for _ in range(10)
]
endStr = input()

for i in range(10):
    if arr[i][-1] == endStr:
        print(arr[i])
    else:
        continue
        print('None')