
from datetime import datetime
# function for hello world

def Hello_world(str):
    print(str)
    return;

Hello_world("Hello world")


#function Time
def time():
    Time_1 = datetime.now().strftime('%H:%M:%S')
    print('current time:',Time_1)

    
time()


# add function

List1=['James', 'John', 'Michael', 'Jean']

   #function
def add(str):
    List1.append(str)
    return;
 

  #used_1
add('Clarence')

print(List1)
 
 #used_2
List1[2]='Jell'
add(List1[2])

print(List1)
    



    

