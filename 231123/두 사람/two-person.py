inp = input().split()
A_age, A_sex =int(inp[0]), inp[1]
B_age,B_sex =int(inp[0]), inp[1]

if A_age>=19 and A_sex=='M'or B_age>=19 and B_sex=='M':
    print(1)
else:
    print(0)