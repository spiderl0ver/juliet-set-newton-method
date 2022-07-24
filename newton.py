import cmath
from graphics import*
win = GraphWin("julietset", 400,400)
win.setCoords(-200,-200,200,200)
# i'm too lazy to code it for other equations
#f(x) = x**3 - 1 you can change it in the parent function
#f'(x) = 3x**2 you can change it in the derivative but it has to be
# the derivative of the parent function, go to math papa
#-1 , 1/2-(sqrt(3)/2)i, 1/2 + (sqrt(3)/2)i

# y is imaginary x is real(EKS - TREAM)
def distance(p,z):
    return cmath.sqrt((p.real-z.real)**2+(p.imag-z.imag)**2)
def parentfunction(x):
    return x**3 - 1
def derivativefunction(x):
    return 3*(x**2)
def newtonmethod(g):
    for i in range(100):
        g = g - (parentfunction(g)/derivativefunction(g))
    return g
for r in range(400):
    r = (r-200)/200
    for i in range(400):
        i = (i-200)/200
        print(r*200,i*200)
        if i ==0 :
            i=0.01
        if r == 0:
            r = 0.01
        number = complex(r,i)
        g = newtonmethod(number)
        print(g)
        if cmath.isclose(complex(1,0),g):
            win.plot(r*200,i*200,"red")
        elif  cmath.isclose(complex(-1/2,-(cmath.sqrt(3)/2)),g):
            win.plot(r*200,i*200,"green")
        else:
            win.plot(r*200,i*200,"blue")


win.getKey()
win.close()

