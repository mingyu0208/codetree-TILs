arr = [ 'L', 'E', 'B', 'R', 'O', 'S']
a = input()
idx = -1

for i in range(0,6):
    if arr[i] == a:
        idx = i

if idx == -1:
    print("None")
else:
    print(idx)