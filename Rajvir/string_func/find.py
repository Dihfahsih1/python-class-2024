#find
string1= "hello, my name is raj."
index =string1.find("my")
print(index)

def replacement():
    sentence = input("Enter any sentence.")
    word_to_find = "my"
    word_to_replace ="your"

    new_word= sentence.find(word_to_find)

    if new_word != -1:
        new_sentence= sentence.replace(word_to_find,word_to_replace)
        print(new_sentence)
    else:
        print(f"{word_to_find} does not exist")
replacement()