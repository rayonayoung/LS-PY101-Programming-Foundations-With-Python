# debug.py

import pdb

counter = 1

pdb.set_trace()  # Another breakpoint

while counter <= 5:
    print(counter)
    pdb.set_trace()  # Add breakpoint
    counter += 1
    
'''def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) > 2:
            word = word.capitalize()
            new_words.append(word)
        else:
            new_words.append(word)

    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))
# titlize(title)'''