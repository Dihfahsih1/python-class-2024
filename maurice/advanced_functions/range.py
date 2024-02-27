# start and end point (it does not include the last no.)
for i in range(2,8):
    print(i)
print ("now stepping")
# steping(skiping some numbers like a sequence) the last number is the number by which we should skip
for i in range(1,10,2):
        print(i)
print("list comprehension")
square=[x**2 for x in range(5)]
print(square)
print("now reversing a range")
# its like counting down 
for i in range(10,0,-2):
      print(i)
print("time to sleep")
for i in range(10,0,-1):
      print(i)
print("SLEEPPPP!!!!")