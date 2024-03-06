#implement a countdownn using a while loop and sleep()
# import time
# countdown = int(input("enter your countdown number"))
# while  countdown >0:
#     print(countdown)
#     countdown -=1
#     time.sleep(1)
# print("blast off")

#create an annonymous function to determine the max and min
ismax = lambda x,y,z : max(x,y,z)
print(ismax(4,6,9))

# ismin = lambda x,y,z: min(x,y,z)
# x = int(input("enter number"))
# y = int(input("enter number"))
# z = int(input("enter number"))
# print(ismin(x,y,z))

#use lambda to find the square root
squareroot1 = lambda x : x**0.5
print(squareroot1(25))

#change from celcius to faranheight
celcius_to_faranheight = lambda c:(9/5)*c+32
print(celcius_to_faranheight(24))