from cmath import cos
import numpy as np
from sympy.abc import x, y
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))

x0 = int(input("x0: "))
y0 = int(input("y0: "))

n = int(input("n: "))
direccionales = []

if n<0 :
    print(n, "no es un valor permitido para n")
    exit

fSymb = a*(x**2 + y**2) + b*x + c*y + d

r = (b**2 + c**2 - 4*a*d)/(4*a**2)

def gradiente(fSymb, x0, y0):
    dxSymb = sp.diff(fSymb, x)
    dySymb = sp.diff(fSymb, y)

    dx = float(dxSymb.subs(x, x0))
    dy = float(dySymb.subs(y, y0))

    gradiente = [dx, dy]
    print(dx, dy)

    ux = dx/np.sqrt(dx**2 + dy**2)
    uy = dy/np.sqrt(dx**2 + dy**2)

    u = [ux, uy]

    return [gradiente, u]

for i in range(n):
    Du =0
    elementos = gradiente(fSymb, x0, y0)

    for j in range(2):
        Du += elementos[0][j] * elementos[1][j]

    direccionales.append(Du)

    x0 += elementos[1][0]
    y0 += elementos[1][1]

    print("(x0,y0) = (", x0, ",", y0, ")")

print(direccionales)


#grafica

fig = plt.figure()
ax = fig.gca(projection='3d')


X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
R = np.arange(0, 2*np.pi, 0.1)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z,linewidth=0, antialiased=False)

# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).


# Repeat all angles for each radius.


# Convert polar (radii, angles) coords to cartesian (x, y) coords.
# (0, 0) is manually added at this stage,  so there will be no duplicate
# points in the (x, y) plane.
'''x = np.append(0, ((b/(2*a))+r*np.cos(angles)).flatten())
y = np.append(0, ((c/2*a)+r*np.sin(angles)).flatten())'''

'''x = np.linspace(-100, 100, 100)
y = np.linspace(-100, 100, 100)

X,Y = np.meshgrid(x,y)'''

# Compute z to make the pringle surface.
z = a*(x**2 + y**2) + b*x + c*y + d


#ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()