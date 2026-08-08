#making a program that is about what you did in summer time
playtime = input("what did you do in the summer time?")
print("great job!")
rating = int(input("rate your summer time from the scale of 1 to 10:"))
if rating >5:
    print("you had a good summer time!")
else:
    print("you had a bad summer time...")
if rating == 10:
    print("you had the best summer time ever!")
if rating ==0:
    print("you had a bad summer time...")
if rating <0:
    print("that is soo sad...")
if rating >10:
    print("WOW!thats amazing!")
if rating ==5:
    print("you had a cool summer time...")