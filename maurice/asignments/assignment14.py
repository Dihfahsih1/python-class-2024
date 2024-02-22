def main():
    original_string=input("Enter text: ..... ")
    print("The original string: ",original_string)
    reversed_text=original_string[::-1]
    print("The reversed Text: ",reversed_text)
    print("The text in capital: ",original_string.upper())
    print("The stripped text: ",original_string.strip("."))
    counting=input("Enter word whose number you want to know: ")
    print("Times appeared: ",original_string.count(counting))



main()
