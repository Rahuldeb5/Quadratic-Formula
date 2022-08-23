print("Quadratic Formula Calculator\n")

import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print("")
print("Your equation is: " + "f(x) = " + str(a) + "x^2 + " + str(b) + "x + " + str(c)+"\n")

disc = (b**2 - (4*a*c))

if disc >= 0:
    x = [((-b + ((math.sqrt(((b ** 2) - (4 * a * c)))))) / (2 * a)), ((-b - ((math.sqrt(((b ** 2) - (4 * a * c)))))) / (2 * a))]
else:
    pass

if disc >= 1:
    print("There are two real solutions")
    print("Real solutions: " + str(x))

elif disc == 0:
    print("There is one real solution")
    if x[0] == x[1]:
        print("Real solution: " + str(x[0]))
    else:
        print("Real solutions: " + str(x))

else:
    print("There are no real solutions")
