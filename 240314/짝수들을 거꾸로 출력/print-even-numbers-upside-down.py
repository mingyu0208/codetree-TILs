given1 = input()
given2 = input()
given_arr = given2.split(' ')

even_arr = []
for elem in given_arr:
    if int(elem) % 2 == 0:
        even_arr.append(elem)

rev_arr = even_arr[::-1]
for e in rev_arr:
    print(e, end=" ")