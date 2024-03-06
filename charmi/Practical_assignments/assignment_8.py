# Program for days of the week.

import datetime

def current_day():

    print("The day today is:")
    
    current_day= datetime.datetime.now()

    if current_day.strftime('%a') == "Mon":
        print("Monday: First day of the week. ")

    elif current_day.strftime('%a') == "Tue":
        print("Tuesday: Second day of the week.")

    elif current_day.strftime('%a') == "Wed":
        print("Wednesday: Mid week.")

    elif current_day.strftime('%a') == "Thur":
        print("Thursday: Assignment day is here.")

    elif current_day.strftime('%a') == "Fri":
        print("Friday: Going for Juma prayers.")

    elif current_day.strftime('%a') == "Sat":
        print("Saturday: Going to Church for prayers.")

    elif current_day.strftime('%a') == "Sun":
        print("Sunday: Last day of the week.")

    else:
        print("Day not found!")

current_day()

    