h,w = map(int,input().split())

bmi = w * (100 ** 2) // (h * h)

print(bmi)
if bmi>25:
    print("Obesity")