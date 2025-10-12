'''Given the following similar sets of code, what will each 
code snippet print?

A)
def mess_with_vars(one, two, three):
    one = two
    two = three
    three = one

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

B)
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")

C)
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")
print(f"two is: {two}")
print(f"three is: {three}")
'''
'''Answer: 
A)

one is ['one']
two is ['two']
three is ['three']

Because the function does not mutate the values, it only reassigns
the local variables.  This doesn't affect the value of the global
variables.

B)
Same answer as A. Global variables are unaffected by updating the
local variables in the function.

C)
one is ['two']
two is ['three']
three is ['one']

The list objects one, two, and three are mutated by the function.
'''



       