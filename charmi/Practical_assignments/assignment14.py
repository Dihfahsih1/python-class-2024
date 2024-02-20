def main():

    input_name= input("Enter your name: ")

    input_name_with_spaces= input("Enter your name with leading spaces: ")

    # performing reverse function
    reversed_name = list(reversed(input_name))   #this operation gives the reversed string in form of a list
    
    #performing uppercase function
    name_in_uppercase = input_name.upper()
    
    #performing lowercase function
    name_in_lowercase = input_name.lower()

    #performing the strip function
    striped_string = input_name_with_spaces.strip(" ")

    #performing the count function
    count_name = str(input_name.count(""))

    #printing all the functions

    print("Your name is: ", input_name)

    print("Your name in upper case looks like this: ", name_in_uppercase)

    print("Your name in lowercase looks like this: ", name_in_lowercase)

    print("The stripped name: ", striped_string)

    print("Your name has: " + count_name + " letters")

main()