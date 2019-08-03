from datetime import datetime
from datetime import timedelta

def DateInput(error = 1):
    """Function to verify that the date inserted is a valid one:
        i.e. in the right form, in numbers, in the future and an existing day 
    """
    """variable 'error' represents if the date is correct (= 0) or not (= 1)
        - error starts = 0
        - error becomes = 1 if an error is spotted
        - while loop runs as long as errors in the input are found.
    """
    while(error == 1):
        error = 0
            
        # check if input is in the right form
        try:
            day, month, year = input("Please insert the date in the form of dd-mm-yyyy: ").split("-")
        except:
            error = 1
            print("You inserted a date in an invalid format.")
        
        # check if only numbers are provided
        if(error == 0):
            if( day.isdigit() and month.isdigit() and year.isdigit() ):
                day = int(day)
                month = int(month)
                year = int(year)
            else:
                error = 1
                print("You should only insert numbers.")

        # check if the input is a valid date
        if(error == 0):
            try:
                date = datetime(day = day, month = month, year = year)
            except:
                error = 1
                print(f"The date {day}/{month}/{year} is not valid.")

        # check if the date is in the past
        if(error == 0):
            if ( not (date < datetime.now()) ):
                error = 1
                print("The date inserted should be in the past")


    date = [day, month, year]
    return date


print("WELCOME IN THE PROGRAM.")
today = datetime.now()
print(f"Today is the {today.day}/{today.month}/{today.year}")

date = DateInput()
print(f"The date inserted is {date[0]}/{date[1]}/{date[2]}.")
















