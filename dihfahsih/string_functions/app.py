def main():
    input_string=input("Enter the string: ")
    
    substring_to_replace=input("Enter sub string to replace: ")
    
    replacement_sub_string=input("Enter the replacement: ")
    
    #perform replacement operation
    replaced_string = input_string.replace(substring_to_replace,replacement_sub_string)
    
    
    #spliting the replaced string into a list of words
    words_list = replaced_string.split()
    
    #join the splitted words with a hyphen
    hyphenated_string = "-".join(words_list)
    
    #output the operations
    print("The String Entered: ", input_string)
    
    print("The replaced String: ", replaced_string )
    
    print("The splitted String: ", words_list)
    
    print("The joined string: ", hyphenated_string)
    
    
main()
    
    
    