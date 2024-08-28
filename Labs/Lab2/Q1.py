# function for trapezoid
def areatrap(b1 ,b2 , h):
    return 0.5 * (b1 + b2) * h

# function for parrallogram
def areaparr(base, height):
    return base * height

# function for volume and S.A of cylinder
def cylinder(radius, hgt):
    pi = 22/7
    volume = pi * radius * radius * hgt
    surfacearea = 2 * pi * radius * (hgt + radius)
    return volume ,surfacearea

# lets pass randomm values for the above functions
b1 = 5
b2 = 6
h = 12
print(f"Area of trapezoid is: {areatrap(b1 ,b2 , h)}")

base = 12
height = 10
print(f"Area of parallelogram is: {areaparr(base, height)}")

radius = 42
hgt = 6
print(f"Volume and Surface Area of clylinder is: {cylinder(radius, hgt)}")
