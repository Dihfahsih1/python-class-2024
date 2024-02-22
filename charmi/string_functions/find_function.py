#find() can also used to get the index

string1= ("hello, my name is           Charmi")

index1=string1.find(" ")
print(index1)                #this will print the index of the first space that occurs

#using find() and replace() under one application

def replacement():

    sentence= input("Enter any sentence of your choice: ")

    word_to_find= input("Enter the word to find from your sentence above: ")

    word_to_replace= input("Enter the word you would want to replace it with: ")

    word_index= sentence.find(word_to_find)

    if word_index != -1:

        new_Sentence= sentence.replace(word_to_find, word_to_replace)
        print(new_Sentence)

    else:
        print(f"The word {word_to_find} does not exist in your sentence!!!")

replacement()

