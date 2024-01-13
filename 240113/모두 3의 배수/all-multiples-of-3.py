sat = False

for i in range(5):
    n= int(input())
    if i%3==0:
        sat = True
        continue
    break


if sat==True:
    print("1")
else:
    print("0")