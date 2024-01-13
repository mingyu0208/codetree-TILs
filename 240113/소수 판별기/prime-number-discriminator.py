n = int(input())

sat =False

for i in range(1,n):
    if i%n==0:
        sat = True



if sat == True:
    print("P")
else:
    print("C")