#find()

string1 = "Hello, how are you ?"
index = string1.find("o",7)

print(index)


Str3= "This is going"
index3=Str3.find("This")

print(index3)


sentence = input("Enter your string : ")
word_to_find = "are"
replacement_word= "is"

index = sentence.find(word_to_find)

if index != -1:
    new_sentence= sentence.replace(word_to_find,replacement_word)
    print(new_sentence)
else:
    print(f"{word_to_find} does not exist in the string")

def replacement():
    User_sentence = input("Enter your sentence : ")
    words_to_find = input("Enter word to find : ")
    words_to_replace= input("Enter word to replace : ")

    index_for_word = User_sentence.find(words_to_find)

    if index_for_word != -1:
        new_user_sentence=User_sentence.replace(words_to_find,words_to_replace)
        print(f"This is your new sentence {new_user_sentence}")
    else:
        print(f"{words_to_find} Is not there in the sentence")

    

replacement()
