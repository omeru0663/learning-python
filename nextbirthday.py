import datetime as dt 
userinput = input("Enter Date Of Birth (dd/mm/yyyy): ")
daysineachmonth = [31,28,31,30,31,30,31,31,30,31,30,31]
totaldays = 0 
day, month, year = userinput.split("/")

monthindex = int(month) 
while monthindex > -1:
    totaldays = totaldays + daysineachmonth[monthindex]
    monthindex = monthindex - 1 

print(f"days until yout birthday: {totaldays}")

