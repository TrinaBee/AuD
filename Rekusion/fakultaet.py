def fakultaet(x):
    if x == 0:
        return 1
    else:
        return x * fakultaet(x - 1)

print(fakultaet(5))