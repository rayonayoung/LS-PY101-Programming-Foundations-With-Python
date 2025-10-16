'''Create a function that takes 2 arguments, a list and a dictionary. 
The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. 
The dictionary will contain two keys, "title" and "occupation", and the appropriate values. 
Your function should return a greeting that uses the person's full name, and mentions the person's title.


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
'''

def greetings(name_list, occupation_dict):
    job_string = ''

    name_string = ' '.join(name_list)

    for entry in occupation_dict:
        job_string += occupation_dict.get(entry) + ' '
    
    print(f'Hello {name_string}! Nice to have a {job_string}around.')

greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)


