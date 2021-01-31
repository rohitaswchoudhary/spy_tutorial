import numpy as np

p = np.poly1d([2,10,12])
print("polynomial is: \n", p)

rootsp = p.r

print("\n Roots of the polynomial: ",rootsp)

# evaluating polynomial at x=2

print("\n evaluating polynomial at x=2: ",p(2))

print("\nCo-efficient of polynomial:", p.c)

# We can also change the variable of the polynomial
np.poly1d.variable='z'

print('\n polynomial with variable z ',p)

# basic arithmatic operations on polynomials

