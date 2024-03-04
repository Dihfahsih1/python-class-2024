from timeit import timeit

  # it is a module used measuring the amount of time a code takes to run

#mysetup = "5+5"
#print(timeit(mysetup))


line = "16-44"
print(f"executing variable line took {timeit(line)}seconds")

line2 = '1+2'
myline = '1+2'
print(timeit(stmt= myline,timer= _timer ,setup= ,number=1))
