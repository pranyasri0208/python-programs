try:
    num1,num2=eval(input("enter two numbers, separated by a comma:"))
    result=num1/num2
    print("the result is:",result)
except ZeroDivisionError:
    print("division by zero is error!!!")
except SyntaxError:
    print("comma is missing!!! enter the comma like this: _,_")
except:
    print("wrong input!!")
else:
    print("no exception")
finally:
    print("this will still execute")