'''
Consider these two simple functions:

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

What will the following function invocation return?

bar(foo())
'''
'''Answer: 

foo() = "yes"

bar("yes") = False and True = False

Output will be False.
'''

       