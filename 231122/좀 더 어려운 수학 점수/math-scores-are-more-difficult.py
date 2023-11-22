inp = input().split()
A_m,A_e = int(inp[0]), int(inp[1])

inp = input().split()
B_m,B_e = int(inp[0]), int(inp[1])

if A_m>B_m or A_m==B_m and A_e>B_e:
    print('A')
else:
    print('B')