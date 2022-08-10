from cmath import sqrt


def almightyFormula(a,b,c):
    x = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    X = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    print('x is ' + str(x))
    print('X is ' + str(X))

almightyFormula(1,0,-4)