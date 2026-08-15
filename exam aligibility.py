medical_cause = input("did u have any medical causes? (Y/N): ").strip().upper()
if medical_cause == "Y":
    print("you are eligible for exam")
else:
    atte=int(input("please enter your attendance percentage: "))
    if atte >= 75:
        print("you are eligible for exam")
    else:
        print("you are not eligible for exam")