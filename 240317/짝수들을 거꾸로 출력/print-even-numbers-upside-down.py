a = int(input())
arr_list = list(map(int,input().split()))
even_arr = []

for i in arr_list:
    if i % 2 == 0:
        even_arr.append(i)



rev_arr = even_arr[::-1]
for e in rev_arr:
    print(e, end=" ")