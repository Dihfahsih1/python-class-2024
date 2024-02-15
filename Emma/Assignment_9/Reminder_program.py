import datetime



days = ["Sunday","Monday"," Tuesday","Wednesday","Thursday","Friday","Saturday"]
days.pop(5)

today= datetime.datetime.now()
print(days[today.weekday()])
print(today)


if today.weekday() == 0:
    print("REMINDER : You have a meeting today")
elif today.weekday()== 1 :
    print("REMINDER: Logistics work at the harbour")
elif today.weekday() == 2:
    print(" REMINDER : Pick Clarence from the airport at 12pm")
elif today.weekday()== 3:
    print("REMINDER : wedding on saturday don't forget")
elif today.weekday() == 4:
    print("REMINDER : go and filter the water tank")
elif today.weekday()== 5:
    print("REMINDER : wedding today go pick up your suit")
elif today.weekday()== 6:
    print("REMINDER : Relax and get ready for monday")
else:
    print("NOTE : There is no such day")

value_date=0
while value_date <= 1:
   value_date += 1
   print("This is your Reminder of the day !!")
   



    
