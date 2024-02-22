def main():
    input_string=input("Enter the string : ")

    substring_to_replace=input("Enter sub string to replace :")

    replacement_substring=input("Enter the replacement : ")

#perform replacement operation
    replaced_string = input_string.replace(substring_to_replace,replacement_substring)


    #splitting the replaced string into a list of words
    words_list = replaced_string.split()

    #join the splitted words with hyphen
    hyphenated_string="-".join(words_list)

    #output the operation
    print("the string entered :", input_string)

    print("The replaced string :", replaced_string)

    print("the splitted string :", words_list)

    print("The joined string :", hyphenated_string)

main()


    
