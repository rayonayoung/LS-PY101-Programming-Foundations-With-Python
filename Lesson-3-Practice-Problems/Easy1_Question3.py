'''Starting with the string:

famous_words = "seven years ago..."

Show two different ways to create a new string with 
"Four score and " prepended to the front of the string 
referenced by famous_words.
'''
famous_words = "seven years ago..."

#Method 1
new_string1 = "Four score and " + famous_words

#Method 2
new_string2 = f'Four score and {famous_words}'

#Method 3
new_string3 = " ".join(["Four score and",famous_words])

print(new_string1)
print(new_string2)
print(new_string3)



