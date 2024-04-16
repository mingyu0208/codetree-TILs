arr = input()
answer = []

for i in range(len(arr)):
    if i%2!=0:
        answer.append(arr[i])
answer.reverse()
print(''.join(answer))