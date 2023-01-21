import math

def area_function():
    A = input("Which plane shape do you want to determine the area: ").lower()
    Response1 = "triangle"
    Response2 = "square"
    Response3 = "circle"
    Response5 = "rectangle"
    Response4 = "invalid entry"
    Unit = " Square Centimetres"
    Response6, Response7, Response8 = "height and breath", "length of two sides and the angle between them", \
                                      "Length of the three sides"
    if A == Response1:
        T = input("Which parameters (Height and Breath or Length of two sides and the Angle between them "
                  "or Length of the three sides) are given: ").lower()
        if T == Response6:
            B = float(input("Height (in cm): "))
            C = float(input("Breath (in cm): "))
            area_of_triangle = 1 / 2 * B * C
            y1 = round(area_of_triangle, 1)  # the round() funtion was used to approximate the area to 1 decimal place
            print(str(y1) + Unit)
        elif T == Response7:
            a1 = float(input("Length of one side (in cm): "))
            a2 = float(input("Length of other side (in cm): "))
            a3 = float(input("Angle: "))
            t1 = math.pi * a3 / 180  # ie, converting angle from rad. to degree
            area_of_triangle = 1 / 2 * a1 * a2 * math.sin(t1)
            y1 = round(area_of_triangle, 1)
            print(str(y1) + Unit)
        else:
            a4 = float(input("Length of first side (in cm): "))
            a5 = float(input("Length of second side (in cm): "))
            a6 = float(input("Length of third side (in cm): "))
            p = (a4 + a5 + a6) / 2
            k = (p - a4) * (p - a5) * (p - a6) * p
            area_of_triangle = math.sqrt(k)
            y1 = round(area_of_triangle, 1)
            print(str(y1) + Unit)
    elif A == Response2:
        D = float(input("Length (in cm): "))
        E = float(input("Breath (in cm): "))
        area_of_square = D * E
        y1 = round(area_of_square, 1)
        print(str(y1) + Unit)
    elif A == Response5:
        D = float(input("Length (in cm): "))
        E = float(input("Breath (in cm): "))
        area_of_rectangle = D * E
        y1 = round(area_of_rectangle, 1)
        print(str(y1) + Unit)
    elif A == Response3:
        F = float(input("Radius (in cm): "))
        area_of_circle = 22 / 7 * F
        y1 = round(area_of_circle, 1)
        print(str(y1) + Unit)
    else:
        print(Response4)

# The string function, str() was used to convert each of the areas from number data type to strings before printing.
# This is because Python can't print numbers and strings joined by + operator.


area_function()  
