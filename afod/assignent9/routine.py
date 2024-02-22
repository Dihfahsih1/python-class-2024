import datetime
def current_day():
    current_day= datetime.datetime.now()

    if current_day.strftime('%a') =="Mon":
        print("monday: First day of the week.")

    if current_day.strftime('%a') == "Tue":
        print("tuesda: second day of the week.")

    if current_day.strftime('%a') == "wed":
        print("wednesday: mid week.")

    if current_day.strftime('%a') == "Thur":
        print("Thursday: Assignment day is here.")

    if current_day.strftime('%a') == "Fri":
        print("Friday : going for juma prayers")

    if current_day.strftime('%a') == "Sat":
        print("Saturday: going to church for prayers")

    if current_day.strftime('%a') == "Sun":
        print("Sunday: its the last day of the week")

    else:
        print("Day not found")

current_day()


