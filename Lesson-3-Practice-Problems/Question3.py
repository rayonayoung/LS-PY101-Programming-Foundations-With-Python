'''How can you determine whether a given string ends 
with an exclamation mark (!)? Write some code that prints
 True or False depending on whether the string ends with an 
 exclamation mark.
 
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False'''

def ends_with_exclamation_mark(str):
    if str[len(str)-1] == '!':
        print('True')
    else:
        print('False')

'''Alternate'''

def ends_with_exclamation_mark_alt(str):
    print(str.endswith('!'))

