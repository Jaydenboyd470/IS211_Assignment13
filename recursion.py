# Part I: Fibonacci sequence
def fibonacci(n):
    """
    Returns the nth element of the Fibonacci sequence using recursion.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Part II: Euclid's GCD Algorithm
def gcd(a, b):
    """
    Returns the greatest common divisor of a and b using Euclid's algorithm recursively.
    """
    if b == 0:
        return a
    return gcd(b, a % b)

# Part III: String Comparison
def compareTo(s1, s2):
    """
    Compares two strings recursively:
    - Returns a negative number if s1 < s2
    - Returns 0 if s1 == s2
    - Returns a positive number if s1 > s2
    """
    if not s1 and not s2:  # Both strings are empty
        return 0
    if not s1:  # s1 is empty, s2 is not
        return -ord(s2[0])
    if not s2:  # s2 is empty, s1 is not
        return ord(s1[0])
    if s1[0] != s2[0]:  # Compare first characters
        return ord(s1[0]) - ord(s2[0])
    # Compare the rest of the strings
    return compareTo(s1[1:], s2[1:])
