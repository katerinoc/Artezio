"""Task 1"""


class Complex:

    """Constructor"""
    def __init__(self, re1, im1, re2, im2):
        self.re1 = re1
        self.im1 = im1
        self.re2 = re2
        self.im2 = im2

    def __add__(self, other):
        return self.other

    def __sub__(self, other):
        return self.other

    def __mul__(self, other):
        return self.other

    def __truediv__(self, other):
        return self.other

    def __mod__(self, other):
        return self.other


print("Введите числа:")
A = Complex(re1=float(input()), im1=float(input()), re2=float(input()),
            im2=float(input()))
A1 = complex(A.re1, A.im1)
A2 = complex(A.re2, A.im2)
print(A1.__add__(A2))
print(A1.__sub__(A2))
print(A1.__mul__(A2))
print(A1.__truediv__(A2))
print(complex(A.re1.__mod__(A.re2), A.im1.__mod__(A.im2)))
print(complex(A.re2.__mod__(A.re1), A.im2.__mod__(A.im1)))
