import datetime
currentyear = datetime.datetime.now().year
userinput = int(input("Enter Year Of Birth: "))
print(f"you are {currentyear - userinput} years old")
