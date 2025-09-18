'''Programmatically determine whether 42 lies between 10 and 
100, inclusive. Do the same for the values 100 and 101.
'''

def is_between(num_a, num_b, num_test):
    if num_test >= num_a and num_test <= num_b:
        print(f'{num_test} is between {num_a} and {num_b}')
    else:
        print(f'{num_test} is NOT between {num_a} and {num_b}')

is_between(10, 100, 42)
is_between(10, 100, 101)
is_between(10, 100, 102)

#Alternate method

print(42 in range(10,100))
print(100 in range(10,100))
print(101 in range(10,100))






