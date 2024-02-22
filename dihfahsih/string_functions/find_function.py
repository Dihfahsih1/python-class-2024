#find()
from advanced_functions import main
sentence=input("Enter your string: ")
word_to_find="are"
replacement_word="is"

index = sentence.find(word_to_find)

if index != -1:
    new_sentence=sentence.replace(word_to_find,replacement_word)
    print(new_sentence)
    
else:
    print(f"{word_to_find} does not exist in the string")