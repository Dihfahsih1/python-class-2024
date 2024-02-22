#write a simple application that performs the following string
#reverse()
#uppercase()
#lowercase()
# strip
#count()
def main():
    input_string = input("enter your string: ")

    reversed_string = input_string[::-1]

    upper_cased_string = reversed_string.upper()

    input_strip_string = input("enter your name begin with equal signs and end with equals")

    sriped_string= input_strip_string.strip("=")

    lowered_string = sriped_string.lower()

    print(input_string)

    print(reversed_string)

    print(upper_cased_string)

    print(input_strip_string)

    print(lowered_string)

main()