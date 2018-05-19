# A regular polygon has n number of sides. Each side has length s.

# The area of a regular polygon is: (.25*n*s**2)/(tan(pi/n))
# The perimeter of a polygon is: length of the boundary of the polygon
# Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.

from math import tan, pi

def polysum(n,s):
    """
    returns the sum of the area and the square of the perimeter of a polygon of n sides
    """
    area = (.25*n*s**2)/(tan(pi/n))
    perimeter = n*s

    return round(area + perimeter**2, 4)




print(polysum(4, 3.5278628762))
