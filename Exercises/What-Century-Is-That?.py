'''Write a function that takes a year as input and returns the century. 
The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate 
for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.'''

def century(year):
    century_number = 1
    suffix = 'th'

    if len(str(year)) >= 3:
        century_number = int(str(year)[0:-2])

        if int(str(year)[-1]) != 0:
            century_number += 1

    match int(str(century_number)[-1]):
        case 1:
            suffix = 'st'
        case 2:
            suffix = 'nd'
        case 3:
            suffix = 'rd'
        case _:
            suffix = 'th'  

    if len(str(century_number)) >= 2 and (int(str(century_number)[-2])== 1):
        suffix = 'th'    
               
    return str(century_number) + suffix

print(century(2000) == "20th")         # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")         # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True