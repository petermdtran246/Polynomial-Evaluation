def power(x, p):
    """
    Calculates the value of x^p for any real number x and any non-negative integer p

    :parameter
    -----------------------------------------------------------------------------------
        x: The base value (real number).
        p: The exponent (non-negative integer).

    :return
    -----------------------------------------------------------------------------------
        The result of x raised to the power p.
    """
    result = 1
    for _ in range(p):
        result *= x
    return result

def polynomial(A, x):
    """
    Evaluates the polynomial represented by the coefficients in array A at the value x.

    :parameter:
    -----------------------------------------------------------------------------------
        a: The array of coefficients.
        x: The value at which to evaluate the polynomial.

    :return:
    -----------------------------------------------------------------------------------
        The result of the polynomial evaluation.
    """
    result = 0
    degree = len(A)  # Calculate the degree of the polynomial
    for k in range(degree): # Iterate over all coefficients
        result += A[k] * power(x, k)  # Calculate term and add to result

    return result

# Coefficients for the polynomial
A = [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9]

# Value to evaluate
x_value = 5.4

# Evaluate the polynomial
result = polynomial(A, x_value)
print(f'The value of the polynomial at x = {x_value} is: {result:.1f}')