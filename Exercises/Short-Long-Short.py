'''Short Long Short
Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the
shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.'''

def short_long_short(string1, string2):
    if len(string1) >= len(string2):
        short_string = string2
        long_string = string1

    else:
        short_string = string1
        long_string = string2

    return short_string + long_string + short_string

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")