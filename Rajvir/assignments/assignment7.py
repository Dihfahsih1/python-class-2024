# PROGRAM FOR DAYS IN A WEEK...
import datetime

def current_day():
  

    current_day= datetime.datetime.now()

    if current_day.strftime("%a") == "Mon":
        print ("Monday: is the first day of the week.")
    
    elif current_day.strftime("%a") == "Tue":
        print (" Tuesday: is the second day of the week.")

    elif current_day.strftime("%a") == "Wed":
        print ("Wednesday: mid week.")

    elif current_day.strftime("%a") == "Thur":
        print ("Thursday: Assignment day is here.")

    elif current_day.strftime("%a") == "Fri":
        print ("Friday: Going for Juma Prayers.")

    elif current_day.strftime("%a") == "Sat":
        print ("Saturday: Going to Church.")

    elif current_day.strftime("%a") == "Sun":
        print ("Sunday:Last day of the week.")
    
    else:
        print("Day not found.")
current_day()