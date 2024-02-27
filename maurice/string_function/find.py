def replacement():
    enter=input("Enter your text: ")
    word_to_find="stay"
    word_to_insert="GO!"
    new_sentence=enter.find(word_to_find)

    if new_sentence != -1:
      final_sentence=enter.replace(word_to_find,word_to_insert)
      print(final_sentence)
    else:
       print(f'{word_to_find} is not in the entered sentence')
replacement()

