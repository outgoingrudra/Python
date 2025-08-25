import math

a, b = 12, 15
lcm = abs(a*b) // math.gcd(a, b)
print("LCM of", a, "and", b, "is", lcm)
