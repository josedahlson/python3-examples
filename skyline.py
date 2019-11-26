# Define a function that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase.
# Testcase: "Hello" -> "hElLo"

def myfunc(mystring):
    index_count = 1
    word = ""
    for letter in mystring:
        index_count += 1
        if index_count % 2 == 0:
            letter = letter.lower()
        elif index_count % 2 == 1:
            letter = letter.upper()
        word += letter
    return word
    
print(myfunc("Hello"))
