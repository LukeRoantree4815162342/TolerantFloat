from math import isclose


class TolerantFloat(float):
    def __init__(self, value, tol=5, show_tol=False):
        self.value = value
        self.tolerance = tol
        self.show_tol=show_tol


    # Handle equality checks
    def __eq__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                left = isclose(self.value, other.value, abs_tol=10**-self.tolerance)
                right = isclose(self.value, other.value, abs_tol=10**-other.tolerance)
                return left and right
            return isclose(self.value, other, abs_tol=10**-self.tolerance)
        except TypeError as e:
            raise

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __le__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return self.value < other.value or self.__eq__(other)
            return self.value < other or self.__eq__(other)
        except TypeError as e:
            raise

    def __ge__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return self.value > other.value or self.__eq__(other)
            return self.value > other or self.__eq__(other)
        except TypeError as e:
            raise

    # Handle addition
    def __add__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(self.value + other.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(self.value + other, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    def __radd__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(self.value + other.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(self.value + other, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    # Handle subtraction
    def __sub__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(self.value - other.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(self.value - other, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    def __rsub__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(other.value - self.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(other - self.value, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    # Handle multiplication
    def __mul__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(self.value * other.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(self.value * other, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    def __rmul__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(self.value * other.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(self.value * other, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    # Handle division
    def __truediv__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(self.value / other.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(self.value / other, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    def __rtruediv__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(other.value / self.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(other / self.value, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    # Handle modulo divisions
    def __mod__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(self.value % other.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(self.value % other, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    def __rmod__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(other.value % self.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(other % self.value, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    # Handle floor divisions
    def __floordiv__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(self.value // other.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(self.value // other, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    def __rfloordiv__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(other.value //self.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(other // self.value, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    # Handle divmod
    def __divmod__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                a,b = divmod(self.value, other.value)
                return a, TolerantFloat(b, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            a,b = divmod(self.value, other)
            return a, TolerantFloat(b, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    def __rdivmod__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                a,b = divmod(other.value, self.value)
                return a, TolerantFloat(b, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            a,b = divmod(other, self.value)
            return a, TolerantFloat(b, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    # Handle exponentiation
    def __pow__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(self.value ** other.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(self.value ** other, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    def __rpow__(self, other):
        try:
            if isinstance(other, TolerantFloat):
                return TolerantFloat(other.value ** self.value, tol=max(self.tolerance, other.tolerance), show_tol=self.show_tol)
            return TolerantFloat(other **  self.value, tol=self.tolerance, show_tol=self.show_tol)
        except TypeError as e:
            raise

    # Handle sign changes
    def __pos__(self):
        return TolerantFloat(self.value, tol=self.tolerance, show_tol=self.show_tol)

    def __neg__(self):
        return TolerantFloat(-self.value, tol=self.tolerance, show_tol=self.show_tol)
    
    def __abs__(self):
        return TolerantFloat(abs(self.value), tol=self.tolerance, show_tol=self.show_tol)
    
    # Handle representation
    def __repr__(self):
        if self.show_tol:
            return f"{self.value} ± 1e-{self.tolerance:02d}"
        return f"{self.value}"