import pytest
from tolerant_float import TolerantFloat
from math import isclose


# instances for tests:
a = TolerantFloat(10, tol=3)
b = TolerantFloat(10.01, tol=1)
c = TolerantFloat(10.0001, tol=1, show_tol=True)

@pytest.mark.equality
def test_equality():
    assert not (a==b), "equality error"
    assert not (b==a), "equality error"
    assert not (a==10.01), "equality error"
    assert not (10.01==a), "equality error"
    assert (b==c), "equality error"
    assert (c==b), "equality error"
    assert (c==10.01), "equality error"
    assert (10.01==c), "equality error"

@pytest.mark.inequality
def test_inequality():
    assert a!=b, "inequality error"
    assert not (b!=c), "inequality error"
    assert a<=b, "inequality error"
    assert not a>=b, "inequality error"
    assert not b<=a, "inequality error"
    assert b>=a, "inequality error"

@pytest.mark.addition
def test_addition():
    assert isinstance(a+1, TolerantFloat), "addition error"
    assert isinstance(1+a, TolerantFloat), "addition error"
    assert isclose((a+b).value, 20.01, abs_tol=1e-10), "addition error"
    assert isclose((b+a).value, 20.01, abs_tol=1e-10), "addition error"
    assert isclose((a+10.01).value, 20.01, abs_tol=1e-10), "addition error"
    assert isclose((b+10).value, 20.01, abs_tol=1e-10), "addition error"
    assert isclose(+a, 10, abs_tol=1e-10), "addition error"

@pytest.mark.subtraction
def test_subtraction():
    assert isinstance(a-1, TolerantFloat), "subtraction error"
    assert isinstance(1-a, TolerantFloat), "subtraction error"
    assert isclose((a-b).value, -0.01, abs_tol=1e-10), "subtraction error"
    assert isclose((b-a).value, 0.01, abs_tol=1e-10), "subtraction error"
    assert isclose((a-10.01).value, -0.01, abs_tol=1e-10), "subtraction error"
    assert isclose((b-10).value, 0.01, abs_tol=1e-10), "subtraction error"
    assert isclose(-a, -10, abs_tol=1e-10), "subtraction error"

@pytest.mark.multiplication
def test_multiplication():
    assert isinstance(a*3, TolerantFloat), "multiplication error"
    assert isinstance(3*a, TolerantFloat), "multiplication error"
    assert isclose((a*b), 100.1, abs_tol=1e-10), "multiplication error"
    assert isclose((b*a), 100.1, abs_tol=1e-10), "multiplication error"

@pytest.mark.truedivision
def test_truedivision():
    assert isinstance(a/3, TolerantFloat), "division error"
    assert isinstance(3/a, TolerantFloat), "division error"
    assert isclose((a/b), 0.999000999000999, abs_tol=1e-10), "multiplication error"
    assert isclose((b/a), 1.001, abs_tol=1e-10), "division error"

@pytest.mark.floordivision
def test_floordivision():
    assert isinstance(a//3, TolerantFloat), "floor division error"
    assert isinstance(3//a, TolerantFloat), "floor division error"
    assert isclose((a//b), 0, abs_tol=1e-10), "floor division error"
    assert isclose((b//a), 1, abs_tol=1e-10), "floor division error"

@pytest.mark.modulodivision
def test_modulodivision():
    assert isinstance(a%3, TolerantFloat), "modulo division error"
    assert isinstance(3%a, TolerantFloat), "modulo division error"
    assert isclose((a%b), 10.0, abs_tol=1e-10), "modulo division error"
    assert isclose((b%a), 0.009999999999999787, abs_tol=1e-10), "modulo division error"

@pytest.mark.divmod
def test_divmod():
    assert isinstance(divmod(a, 3), tuple), "divmod error"
    assert isinstance(divmod(3, a), tuple), "divmod error"
    assert isinstance(divmod(a, 3)[0], int), "divmod error"
    assert isinstance(divmod(a, 3)[1], TolerantFloat), "divmod error"

@pytest.mark.exponentiation
def test_exponentiation():
    assert isinstance(a**3, TolerantFloat), "exponentiation error"
    assert isinstance(3**a, TolerantFloat), "exponentiation error"
    assert isclose(a**1.2, 15.848931924611133, abs_tol=1e-10), "exponentiation error"
    assert isclose(1.2**a, 6.191736422399997, abs_tol=1e-10), "exponentiation error"

@pytest.mark.signchange
def test_signchange():
    assert isinstance(+a, TolerantFloat), "sign change error"
    assert isinstance(-a, TolerantFloat), "sign change error"
    assert isclose(-a, -10, abs_tol=1e-10), "sign change error"
    assert isclose(+a, 10, abs_tol=1e-10), "sign change error"  
    assert isinstance(abs(a), TolerantFloat), "sign change error"
    assert isclose(abs(a), 10, abs_tol=1e-10), "sign change error"

@pytest.mark.representation
def test_representation():
    assert isinstance(a, TolerantFloat), "representation error"
    assert f"{a}" == '10', "representation error"
    assert f"{b}" == '10.01', "representation error"
    assert f"{c}" == '10.0001 ± 1e-01', "representation error"