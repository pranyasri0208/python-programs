for x in range(25):
    if x % 20==0:
        print(x,"twist")
    elif x % 15==0:
        pass
    elif x % 5==0:
        print(x, "fizz")
    elif x % 3==0:
        print(x, "buzz")
    else:
        print(x)