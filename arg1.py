def total_calc(x,y):
    total = x + x * y /100
    total = round(total, 0)
    print("please pay $", total, sep="")

total_calc(150,20)