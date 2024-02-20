def main():
    input_str = str(input("Enter a string: "))
    sub_str_to_replace = str(input("Enter substring to replace: "))
    
    replacement_sub_str = str(input("Enter the replacement: "))
    # perform replacement operation
    replaced_str = input_str.replace(sub_str_to_replace, replacement_sub_str)
    
    
    # spliting the replaced str into a list of words
    words_list = replaced_str.split()
    
    # join the splitted words with a hyphen
    hypenated_str = "-".join(words_list)
    # output the operations
    print(f"The string entered is: {input_str}")
    print(f"The replaced string: {replaced_str}")
    print(f"The splitted string: {words_list}")
    print(f"The joined string: {hypenated_str}")
    
main()
    