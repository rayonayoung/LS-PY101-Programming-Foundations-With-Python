'''
What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)
'''
'''Answer: 
The last line will output:
{'first':[1, 2]}
Because num_list points to the same object as the value for the 
'first' key in the dictionary. So when num_list is mutated, that
value is changed.
'''

       