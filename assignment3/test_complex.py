from complex import Complex

# Asserts calculations for addition and chechking equality by the string
def testAddition():
    assert str(Complex(1, 2) + Complex(1, 2)) == "2+4i"
    assert str(Complex(0, -9) + Complex(-5, 4)) == "-5-5i"
    assert str(Complex(5, 0) + Complex(2, 4)) == "7+4i"

# Asserts calculations for subtraction and checking equality by the string
def testSubtraction():
    assert str(Complex(3, 0) - Complex(4, -1)) == "-1+1i"
    assert str(Complex(2, -9) - Complex(-5, 4)) == "7-13i"
    assert str(Complex(0, 8) - Complex(2, 4)) == "-2+4i"

# Asserts calculations for conjugation and checking equality by the string
def testConugation():
    assert str(Complex(3, 2).conjugate()) == "3-2i"
    assert str(Complex(2, -9).conjugate()) == "2+9i"
    assert str(Complex(5, 0).conjugate()) == "5+0i"

# Asserts calculations for modulus
def testModulus():
    assert Complex(3, 4).modulus() == 5
    assert Complex(6, -8).modulus() == 10
    assert Complex(0, 8).modulus() == 8

# Asserts different scenarios for equality
def test__eq__():
    assert Complex(1, 2) == Complex(1, 2)
    assert Complex(0, 8.0) == Complex(0, 8)
    assert Complex(2, 4) != Complex(4, 4)

# Asserts calcutations for multiplication
def testMultiplication():
    assert Complex(1, 2) * Complex(1, 2) == Complex(-3, 4)
    assert Complex(3, 5) * Complex(-1, 3) == Complex(-18, 4)

# Asserts calculations for addition with ints/floats and Python's complex numbers
def testAdditionWithPythonComplex():
    assert Complex(1, 2) + complex(4, 5) == Complex(5, 7)
    assert Complex(4, 9.43) + (2+3j) == Complex(6, 12.43)
    assert complex(-2, 6) + Complex(9, 10) == Complex(7, 16)
    assert 4 + Complex(3, 8) == Complex(7, 8)

# Asserts calculations for subtraction with ints/floats and Python's complex numbers
def testSubtractionPythonComplex():
    assert Complex(1, 2) - (3+9j) == Complex(-2, -7)
    assert Complex(10, 7) - 5.6 == Complex(4.4, 7)
    assert (8+7j) - Complex(1,2) == Complex(7, 5)

# Asserts calculations for multiplication with ints/floats and Python's complex numbers
def testMultiplicationWithPythonComplex():
    assert Complex(1, 2) * complex(1, 2) == Complex(-3, 4)
    assert Complex(3, 5) * complex('-10-7j') == Complex(5, -71)
    assert (3+5j) * Complex(-10, -7) == Complex(5, -71)
    assert 2j * Complex(-9, 0) * 2j == Complex(36, 0)
    assert Complex(1, 2) * 0 == Complex(0, 0)
