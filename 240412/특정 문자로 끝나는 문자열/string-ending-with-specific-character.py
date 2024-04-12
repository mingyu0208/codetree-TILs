arr = [
    input()
    for _ in range(10)
]
endStr = input()
cnt = 0

for i in range(10):
    if arr[i][-1] == endStr:
        print(arr[i])
        cnt+=1

if cnt==10:
    print('None')