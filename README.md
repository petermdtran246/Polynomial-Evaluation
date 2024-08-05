# Polynomial Evaluation
This repository contains a Python implementation for evaluating polynomials. The polynomial is represented by an array of coefficients, and the evaluation is done using a custom power function to avoid using Python's built-in exponentiation operator.

# Features
  1.  Power Calculation: A function to calculate the power of a real number using a brute-force approach.
  2.  Polynomial Evaluation: A function to evaluate a polynomial at a given value using the custom power function.
  3.  Asymptotic Analysis: An analysis of the number of multiplications required for evaluating a polynomial of degree n.

# Polynomial Representation
A polynomial can be represented as an array where the coefficient of the k-th power of the variable is stored in array entry A[k]. For example, the array:

k	        0	      1	      2	      3	        4	        5	        6
A	      12.3	   40.7	  -9.1	    7.7	      6.4	       0	      8.9

represents the polynomial:
f(x) = 12.3 + 40.7x - 9.1x^2 + 7.7x^3 + 6.4x^4 + 8.9x^6

# Code
The main script polynomial_evaluation.py contains the implementation of the power function and the polynomial evaluation function.

# Functions
power(x, p): Calculates the value of x^p using a brute-force method.
polynomial(A, x): Evaluates the polynomial represented by the array A at the value x.

# Asymptotic Analysis
The maximum number of multiplications needed for any polynomial of degree n is given by the sum of multiplications performed in the power function and the multiplications involved in evaluating the polynomial. For a polynomial of degree n, the total number of multiplications is O(n^2).
