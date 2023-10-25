import math 
radius = float(input("What's Your Radius? "))
area = math.pi*(radius**2)
circumference = 2*(math.pi*radius)
if radius > 0:
    print(f"Your Circumference is {circumference} Your Area is {area}")
