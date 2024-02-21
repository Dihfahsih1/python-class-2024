def app():
 # this is a reverse technique.. reverses the order of the data elements in place.
    sentence = input("Enter a short sentence: ")
    reversed_string= list(reversed(sentence))

 # this is for uppercase...
    upper_case = sentence.upper()
 # this is for lowercase..
    lower_case= upper_case.lower()
 # strip...
    word = ("    banana     ")
    strip_sen = word.strip()
 # count
    count_sen = strip_sen.count("")

    print("the reversed sentence: ", reversed_string)
    print("the cap sentence: ", upper_case)
    print("the lowercase sentence: ", lower_case)
    print("the striped sentence: ", strip_sen)
    print("sentence using count, will have: ", count_sen)


app()
 