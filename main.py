from datetime import datetime
from datetime import timedelta

def DateInput(day=0, month=0, year=0):
    """Function to verify that the date inserted is a valid one:
        - in the right form
        - numbers
        - in the future
        - an existing day """

    # check if input is in the right form
    try:
        day, month, year = input("Please insert the date in the form of dd/mm/yyyy: ").split("/")
    except:
        print("You inserted an invalid date.")
        return False

    # check if only numbers are provided
    if( not(day.isdigit() and month.isdigit() and year.isdigit()) ):
        print("You should only insert numbers.")
        return False
    else:
        day = int(day)
        month = int(month)
        year = int(year)

    # check if the input is in the past.
    today = datetime.now()
    if(year > today.year):
        print("You should put a date in the future")
        return False
    elif( (year == today.year) and (month > today.month) ):
        print("You should put a date in the future")
        return False
    elif( (year == today.year) and (month == today.month) and (day > today.day) ):
        print("You should put a date in the future")
        return False

    # check if the input is a valid date
    try:
        datetime(day = day, month = month, year = year)
        return True
    except:
        print(f"The date {day}/{month}/{year} is not valid.")
        return False


print("WELCOME IN THE PROGRAM.")
today = datetime.now()
print(f"Today is the {today.day}/{today.month}/{today.year}")

while(True):
    if(DateInput()):
        break
















