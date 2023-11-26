A_age, A_sex = int(input()), input()
B_age, B_sex = int(input()), input()

if (A_age or B_age>=19 ) and (A_sex or B_sex=="M"):
    print(1)
else:
    print(0)