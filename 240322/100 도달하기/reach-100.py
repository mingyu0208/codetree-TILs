n = int(input())
new_list = []

new_list.append(1)
new_list.append(n)

for i in range(2,10):
    new_list.append(new_list[i-1]+ new_list[i-2])
    if new_list[i]>100:
        break
for elem in new_list:
    print(elem,end=" ")