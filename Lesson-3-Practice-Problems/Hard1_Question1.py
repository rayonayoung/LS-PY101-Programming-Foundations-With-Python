'''
Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())
'''
'''Answer: 

first() will return {'prop1': "hi there"} but second() will return 
None.  This is due to the placement of the return keyword.  In
second(), return is on it's own line so it is not associated with 
the dictionary.  Those lines in the function are unreachable as 
they occur after the return statement.
'''

       