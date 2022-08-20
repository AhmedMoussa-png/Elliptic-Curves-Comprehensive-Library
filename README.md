# Elliptic-Curves-Comprehensive-Library
This code is aimed at replacing the manual and tedious computations associated with the elliptic curves. The module is equiped with several useful utilities for group operations on points on elliptic curves:
1. **Finding points on an elliptic curve defined by Weierstrass equation.**
2. **Testing whether the curve is *singular* or *non-singular*.**
3. **Finding all pairs of *(a,b)* for curves defined over a prime number *p*.**
4. **Finding non-singular curves defined over the prime *p* with *n* points.**
5. **Performing group law over points belonging to the elliptic curve.**
6. **Scalar multiplication of points.**
7. **Finding order of a point.**
8. **Finding points that generate the elliptic curve.**
9. **Generating Public-key for Elgamal Encryption scheme.***
10. **Encrypting and Decrypting data represented as points on the elliptic curve using Elgamal Encryption scheme.**

## Generating Elliptic Curves
An elliptic curve defined using **Weierstrass equation** is represented by the following equation: 
<p align="center">
  y^2 = x^3+ax+b
</p>
The coordinates *(x,y)* and the constants *a and b* belong to the integers modulo *p*, where *p* is some prime number. Let's start by creating an instance of elliptic curves. The first argument passed will be the constant *a*, the second is the constant *b*, and the third argument will be the prime number *p* over which the elliptic curve is defined:

```
import EllipticCurves
my_curve = EllipticCurves.ELL_CURVES(1,1,5)
```
This is the following elliptic curve:
<p align="center">
  y^2 = x^3+x+1
</p>
defined over the integers modulo *5*.
