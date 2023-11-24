import datetime
currentyear = datetime.datetime.now().year
currentmonth = datetime.datetime.now().month 
currentday = datetime.datetime.now().day
userinput = input("Enter Year Of Birth (dd/mm/yyyy): ")

day, month, year = userinput.split("/")
dayborn = int(day)
monthborn = int(month)
yearborn = int(year)
if yearborn < 100 and yearborn > 24:
    yearborn = yearborn + 1900
elif yearborn <= 23:
    yearborn = yearborn + 2000
else:
    yearborn = yearborn + 0
 
if dayborn - currentday <= 0 and monthborn - currentmonth <= 0:
    age = currentyear -  yearborn
else: 
    age = currentyear - yearborn - 1 

print(f"you are {age} years old")
