from math import pi, sqrt
def area(r,shape):
    return r*r*shape

def area_square(r) :
    return area(r,1)
def area_circle(r):
    return area(r,pi)
    