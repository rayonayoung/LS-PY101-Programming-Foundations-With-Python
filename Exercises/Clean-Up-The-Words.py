'''Given a string that consists of some words and an assortment of non-alphabetic characters, 
write a function that returns that string with all of the non-alphabetic characters replaced by spaces. 
If one or more non-alphabetic characters occur in a row, you should only have one space in the result 
(i.e., the result string should never have consecutive spaces).

Example
print(clean_up("---what's my +*& line?") == " what s my line ") # True'''

def clean_up(string):
    cleaned_string = ''

    for char in string:
        if char.isalpha():
            cleaned_string += char
        else:
            cleaned_string += ' '
    
    result_string = ''
    prev = ''

    for char in cleaned_string:
        if char.isspace() and prev == ' ':
            continue
        else:
            result_string += char
        prev = char
    return result_string

print(clean_up("---what's my +*& line?") == " what s my line ") # True