import math

x, y = 17, 4
print("Remainder of", x, "/", y, "=", math.remainder(x, y))

z = 12.56
frac, whole = math.modf(z)
print("Fractional:", frac, "Whole:", whole)
