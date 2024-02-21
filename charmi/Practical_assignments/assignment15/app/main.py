#this program gives a range of numbers with a power of the user's choice
def main():

# inputing the necessary numbers
    y= int(input("Enter the power of your choice: "))

    input_start_value= int(input("Enter the start value in the range: "))

    input_end_value= int(input("Enter the end value in the range: "))

    input_step_value= int(input("Enter the step value in the range: "))

#function that calculates and gives the range of values
    power= [x**y for x in range(input_start_value, input_end_value, input_step_value)]

#output of the list
    print(f"Your answer is: {power}")

main() 

