import math

class Complex:
    """
    Complex is a class containing complex numbers
    
    The class consists of a constructor, methods for addition, subtraction, multiplication,
    conjugation, modulus, equals and a toString.
    """

    def __init__(self, reNum, imNum):
        """
        __init__ Constructor for Complex
        
        Args:
            reNum (int): Real number
            imNum (int): Imaginary number
        """
        self._reNum = reNum
        self._imNum = imNum

    def __str__(self):
        """
        __str__ toString for Complex to print a understandable string
        
        Returns:
            String: formated string depending the complex number
        """
        #When b is negative
        if self._imNum < 0:
            return str(self._reNum) + str(self._imNum) + "i"
        #When b is zero
        if self._reNum == 0:
            return str(self._imNum) + "i"
        return str(self._reNum) + "+" + str(self._imNum) + "i"

    # Assignment 3.3
    def conjugate(self):
        """
        conjugate Conjugates the complex number
        
        Returns:
            Complex: The complex number is now conjugated
        """
        return Complex(self._reNum, -self._imNum)

    def modulus(self):
        """
        modulus Does the modulus function on the complex number
        Here is math imported to be able to use .sqrt()
    
        Returns:
            int: the length of the line, when considered as a point in the complex plane.
        """
        return math.sqrt(self._reNum ** 2 + self._imNum ** 2)

    
    def __add__(self, other):
        """
        __add__ makes it possible to arithmetically add integers and and Python's complex numbers
        with this class for complex numbers additionally to itself.
        
        Args:
            other (float/complex/Complex): Can be float, Python's complex number or Complex number of this class
        
        Returns:
            Complex: A complex number that has been added by "other"
        """
        if isinstance(other, float) or isinstance(other, int):
            return Complex(self._reNum + other, self._imNum)
        if isinstance(other, complex):
            return Complex(self._reNum + other.real, self._imNum + other.imag)
        return Complex(self._reNum + other._reNum, self._imNum + other._imNum)

    def __sub__(self, other):
        """
        __sub__ Allows arithmetical subtraction with integers and complex numbers
        
        Args:
            other (float/Complex/complex): Can be float, Python's complex number or Complex number of this class
        
        Returns:
            Complex: A complex number that has been subtracted by "other"
        """
        return self + other.__neg__()

    def __mul__(self, other):
        """
        __mul__ Allows arithmetical multiplication with integers and complex numbers
        
        Args:
            other (float/Complex/complex): Can be float, Python's complex number or Complex number of this class
        
        Returns:
            Complex: A complex number that has been multiplied by "other"
        """
        if isinstance(other, float) or isinstance(other, int):
            return Complex(self._reNum * other, self._imNum * other)

        if isinstance(other, complex):
            a = self._reNum * other.real
            b = self._reNum * other.imag
            c = self._imNum * other.real
            d = self._imNum * other.imag
            return Complex(a - d, c + b)

        a = self._reNum * other._reNum
        b = self._reNum * other._imNum
        c = self._imNum * other._reNum
        d = self._imNum * other._imNum
        return Complex(a - d, c + b)

    def __eq__(self, other):
        """
        __eq__ Allows comparisons by value instead of object
        
        Args:
            other (Complex): a complex number of this class to compare
        
        Returns:
            True: if both real number and imaginary number is equal, false if otherwise
        """
        return self._reNum == other._reNum and self._imNum == other._imNum

    # Assignment 3.4
    def __radd__(self, other):
        """
        __radd__ Allows addition for integers and Python's complex numbers
        
        Args:
            other (float/complex): float or Python's complex number
        
        Returns:
            Complex: Complex number added by "other"
        """
        return self + other

    def __rmul__(self, other):
        """
        __rmul__ Allows multiplication for integers and Python's complex numbers
        
        Args:
            other (float/complex): float or Python's complex number
        
        Returns:
            Complex: Complex number multiplied by "other"
        """
        return self * other
        
    def __rsub__(self, other):
        return -self + other

    # Optional, possibly useful methods

    # Allows you to write `-a`

    def __neg__(self):
        """
        __neg__ Negates the complex number
        
        Returns:
            Complex: negated complex number
        """
        return Complex(-self._reNum, -self._imNum)
        

    # Make the `complex` function turn this into Python's version of a complex number
    def __complex__(self):
        """
        __complex__ converts this complex number into Python's version of a complex number
        
        Returns:
            complex: Python's complex number
        """
        return complex(self._reNum, self._imNum)
