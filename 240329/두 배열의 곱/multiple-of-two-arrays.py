arr_d1 = [
    list(map(int,input().split()))
    for _ in range(3)
]

input()

arr_d2 = [
    list(map(int,input().split()))
    for _ in range(3)
]

arr_d3 = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr_d3[i][j] = arr_d1[i][j] * arr_d2[i][j]

for i in arr_d3:
    for elem in i:
        print(elem,end=" ")
    print()