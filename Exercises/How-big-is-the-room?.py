'''How big is the room?
Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

Note: 1 square meter == 10.7639 square feet'''

length = float(input('Enter the length of the room: '))
width = float(input('Enter the widgth of the room: '))
FT2_TO_M2 = 10.7639

area_in_m2 = length * width
area_in_ft2 = area_in_m2 * FT2_TO_M2

print(f'The area of the room is {area_in_m2} square meters, {area_in_ft2} square feet.')
