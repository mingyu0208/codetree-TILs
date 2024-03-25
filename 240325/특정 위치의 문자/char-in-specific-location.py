arr = [ 'L', 'E', 'B', 'R', 'O', 'S']
a = input()

for i in range(0,5):
    if arr[i] == a:
        print(arr.index(a))
    else:
        print('None')