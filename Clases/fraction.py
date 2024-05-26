#clase para operaciones matematicas con fracciones


from __future__ import annotations


class Fraction:
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den
    def __add__(self, other: Fraction):
        if self.den == other.den:
            self.num = self.num + other.num
            self.den = self.den
        else:
            result_den = self.gcd(self.den, other.den)
            arriba = (result_den//self.den) * self.num
            self.num = arriba
            arriba_other = (result_den//other.den) * other.num
            other.num = arriba_other
            self.num = self.num + other.num
        num, den = self.simplificar(self.num, self.den)
        return num, den

    def __sub__(self, other: Fraction):
        if self.den == other.den:
            self.num = self.num - other.num
            self.den = self.den
        else:
            result_den = self.gcd(self.den, other.den)
            arriba = (result_den//self.den) * self.num
            self.num = arriba
            arriba_other = (result_den//other.den) * other.num
            other.num = arriba_other
            self.num = self.num - other.num
        num, den = self.simplificar(self.num, self.den)
        return num, den

    def __mul__(self, other):
        self.num = self.num * other.num
        self.den = self.den * other.den
        num, den = self.simplificar(self.num, self.den)
        return num, den

    def __truediv__(self, other):
        self.num = self.num * other.den
        self.den = self.den * other.num
        num, den = self.simplificar(self.num, self.den)
        return num, den

    def __str__(self):
       return f'{self.num} / {self.den}'

    @staticmethod
    def gcd(a: int, b: int) -> int:
        A = max(a, b)
        B = min(a, b)
        while B:
            mcd = B
            B = A % B
            A = mcd
        mcm = (a * b) // mcd
        return mcm
	
    @staticmethod
    def simplificar(x, y):
        def mcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        comun = mcd(x, y)
        num = x // comun
        den = y // comun
        return num, den


fraction1 = Fraction(25, 30)
fraction2 = Fraction(40, 45)

print(fraction2)