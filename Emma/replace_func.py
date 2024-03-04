string1 = "They are going out"
string2= string1.replace("They","You")
string3 = string2.split(",")

if string3[-1] != "?":
    string3.append("?")
   
    print(string3)
    print(string3[0],string3[-1])

