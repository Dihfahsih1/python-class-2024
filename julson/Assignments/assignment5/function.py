#Hello World 

import datetime
import time


def greetings():
   "This is docstring of greetings function"
   print ("Hello World")
   return

greetings()

#display time

def cureent_time_datime():
   now = time.localtime()
   tt = time.strftime( now)
   print("Current time :", tt)


# adding to a funtion
   
   def testfunction(arg):
      print ("Inside function:",arg)
   print ("ID inside the function:", id(arg))
   arg=arg.append(100)
   
   var=[10, 20, 30, 40]
   print ("ID before passing:", id(var))
   testfunction(var)
   print ("list after function call", var)