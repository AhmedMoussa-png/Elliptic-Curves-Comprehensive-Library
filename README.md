# Elliptic-Curves-Comprehensive-Library
This code is aimed at replacing the manual and tedious computations associated with the elliptic curves. The module is equiped with several useful utilities for group operations on points on elliptic curves:
1. **Finding points on an elliptic curve defined by Weierstrass equation.**
2. **Testing whether the curve is *singular* or *non-singular*.**
3. **Finding all pairs of *(a,b)* for _non-singular_ curves defined over a prime number *p*.**
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
The coordinates (x,y) and the constants a and b belong to the integers modulo p, where p is some prime number. Let's start by creating an instance of elliptic curves. The first argument passed will be the constant a, the second is the constant b, and the third argument will be the prime number p over which the elliptic curve is defined:

```
import EllipticCurves
my_curve = EllipticCurves.ELL_CURVES(1,1,5)
```
This is the following elliptic curve:
<p align="center">
  y^2 = x^3+x+1
</p>
defined over the integers modulo 5.

## Points on the elliptic curve

After creating our object *my_curve*, we can access one of its attributes which is the set of points that belong to the curve:

```
print(my_curve.points)
```

This will ouput the following list of coordinates for points on the elliptic curve:

```
[['INFINITY', 'INFINITY'], [0, 1], [0, 4], [2, 1], [2, 4], [3, 1], [3, 4], [4, 2], [4, 3]]
```

## Discriminant of the Elliptic Curve:

The following method returns a boolean value. If the curve is _non-singular_, it will return a _True_ value. If the curve is _singular_, it will return a _False_ value.

```
non_singular_curve = EllipticCurves.ELL_CURVES(1,1,5)
print(non_singular_curve.discriminant())
```

```
True
```

## Pairs of (a,b) constants that define non-singular elliptic curves over the prime field _p_

We want to find all _non-singular_ curves defined over some prime numbe _p_. In other words we want to find a list of pairs _(a,b)_ that produce _non-singular_ curves. To do this, we will initiate an instance of an elliptic curve defined over the prime _p_ with arbitary constants. Then, we will use the following method to get all possible pairs of _(a,b)_:

```
import EllipticCurves
arbitary_curve = EllipticCurves.ELL_CURVES(1,1,11)
print(arbitary_curve.curves())
```

```
[(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8), (6, 9), (6, 10), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9), (7, 10), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8), (8, 9), (8, 10), (9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8), (9, 9), (9, 10), (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10)]
```
Each entry in this list represents a pair of constants _(a,b)_ for some _non-singular_ elliptic curve defined over the prime _p_.

## Finding the proper _(a,b)_ for an elliptic curve defined over _p_ with _n_ points over it
Suppose we want to find a specific curve with _n_ points defined over the prime _p_. We can find such curve by again initiating an arbitary curve and using the following method to find all possible curves:

```
import EllipticCurves
arbitary_curve = EllipticCurves.ELL_CURVES(1,1,11)
print(arbitary_curve.find_curve(9))
```

```
{(9, 9), (7, 10), (6, 8), (10, 7), (1, 4), (8, 6), (2, 2), (5, 3), (4, 1), (3, 5)}
```
Each element in this set represent a pair of constants _(a,b)_ for a _non-singular_ curve defined over the prime number _11_ with _9_ points on it.

## Performing group law over points belonging to the elliptic curve
The following method is used to add two points on an elliptic curve. It takes two arguments, each of them must be a list of the coordinates of the points to be added:
```
import EllipticCurves
my_curve = EllipticCurves.ELL_CURVES(1,1,11)
print(my_curve.addition([1,5],[3,3]))
```
```
[8, 2]
```

You can also use the following method to double a point:

```
import EllipticCurves
my_curve = EllipticCurves.ELL_CURVES(1,1,11)
print(my_curve.double([1,5]))
```
```
[3,3]
```
## Scalar Multiple of a point
To find the scalar multiple of a point by an integer, we will use the method _scalar_multiple_ which takes two arguments. The first argument is the the point itself and the second arugment is the integer:
```
import EllipticCurves
my_curve = EllipticCurves.ELL_CURVES(1,1,11)
print(my_curve.scalar_multiple([1,5],4))
```
```
[6,5]
```
## Order Of Point
You can find the order of any point on the elliptic curve using the following method:
```
import EllipticCurves
my_curve = EllipticCurves.ELL_CURVES(1,1,11)
print(my_curve.order_of_point([1,5]))
```
```
14
```
## Generator points
Points that generate the elliptic curves are points whose multiples produce all points on the curve. Each curve initiated has an attribute that is a list of the generator points:
```
import EllipticCurves
my_curve = EllipticCurves.ELL_CURVES(1,1,11)
print(my_curve.generators)
```
```
[[1, 5], [1, 6], [4, 5], [4, 6], [8, 2], [8, 9]]
```
## Generating Public key
Each communicating party will have to make public a randomly generated public key for anyone to be able to communicate with them. The public key consists of a randomly generated point _P_ that can be generated using the method _.random_point()_, which takes no arguemnts, and another image point _B_ which is some multiple of _P_. To generate _B_, each communicating party generates a random integer (which will be the private key) _s_ using the method _.random_s()_. Then, we use the method _.gen_public_key()_ to generate _B_.

```
import EllipticCurves
my_curve = EllipticCurves.ELL_CURVES(1,1,11)
P = my_curve.random_point()
s = my_curve.random_s()
B = my_curve.gen_public_key()
verify = my_curve.scalar_multiple(P, s)
print(verify)
print("Your public key is as the following:\n"
      f"P = {P} (public)\n"
      f"B = {B} (public)\n"
      f"s = {s} (secret/private)")
```
```
[0, 1]
Your public key is as the following:
P = [1, 6] (public)
B = [0, 1] (public)
s = 6 (secret/private)
```
