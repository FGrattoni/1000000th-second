from datetime import datetime
from datetime import timedelta


def DateInput():
    """Function to verify that the date inserted is a valid one:
        i.e. in the right form, in numbers, in the future and an existing day 
    """
    while(True):
            
        # check if input is in the right form
        try:
            day, month, year = input("Please insert the date in the form of dd-mm-yyyy: ").split("-")
        except:
            print("You inserted a date in an invalid format.")
            continue
        
        # check if only numbers are provided
        if( day.isdigit() and month.isdigit() and year.isdigit() ):
            day = int(day)
            month = int(month)
            year = int(year)
        else:
            print("You should only insert numbers.")
            continue

        # check if the input is a valid date
        try:
            date = datetime(day = day, month = month, year = year)
        except:
            print(f"The date {day}/{month}/{year} is not valid.")
            continue

        # check if the date is in the past
        if ( not (date < datetime.now()) ):
            print("The date inserted should be in the past")
            continue
        else:
            break

    return date


if __name__ == "__main__":
    print("\nWELCOME IN THE PROGRAM.")
    today = datetime.now()
    print(f"Today is the {today.day}/{today.month}/{today.year}\n")

    date = DateInput()
    print(f"The date inserted is {date.day}/{date.month}/{date.year}.\n")

    print("Would you like the program to consider also the time of the event?") 
    print(f"If no then the program will consider {date.day}/{date.month}/{date.year} 12:00am as the starting date.")
    timeAnswer = input("Answer by y/n: ")

    while(timeAnswer not in ["y", "n", "Y", "N"]):
        timeAnswer = input("Please insert a valid answer y/n: ")

    if(timeAnswer=="y"):
        pass

    date = date.replace(hour=hour, minute=minute)
    print(f"Good, the date considered will be: ")

    
















