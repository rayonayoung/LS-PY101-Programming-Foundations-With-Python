'''Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. 
The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, 
and the other end at the upper-right.

Example 1
triangle(5)
Output for Example 1
    *
   **
  ***
 ****
*****'''

def triangle(size):

    for line in range(size,0,-1):
       print(f'{(' ' * (line - 1)) + (size - line + 1) * '*'}')

triangle(5)


