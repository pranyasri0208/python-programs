string=input("enter a string:")
character=input("enter a character to find its occurance:")
i=0
count=0
while (i<len(string)):
    if string[i]==character:
        count+=1
    i+=1
print("the occurance of the given character is:",count)