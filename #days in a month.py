#Tittle and specify month requirements
print("""
Number of days in a month
=========================
January = 1
February = 2
March = 3
April = 4
May = 5
June = 6
July = 7
August = 8
September = 9
October = 10
November = 11
December = 12 
""")
#Declare month
month = int(input("month: "))
#Determine number of days in month
if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
    days = '31'
elif month == 4 or 6 or 9 or 11:
    days = '30'
elif month == 2:
    lunar = input("Is it a lunar year? yes or no: ")
    if lunar == yes:
        days = '28'
    elif lunar == no:
        days = '30'
else:
    days = 'Please read the requirements on the top!'
#Output number of days
print("There are", days, "days")