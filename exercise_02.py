class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def handle_imaginary(self, i):
        i = int(i.replace('i', ''))
        return i

    def operation(self, a, b, operator):
        try:

            if 'i' in self.a and 'i' in self.b:  # imaginary to imaginary
                ai = self.handle_imaginary(self.a)
                bi = self.handle_imaginary(self.b)
                ans = eval(f'{ai} {operator} {bi}')
                print(f'{self.a} {operator} {self.b} = {ans}i')
            elif isinstance(int(self.a), int) and isinstance(int(self.b), int):  # int to int
                ans = round(eval(f'{a} {operator} {b}'), 2)
                print(f'{self.a} {operator} {self.b} = {ans}')

        except ValueError:  # int to imaginary
            print(f'{self.a} {operator} {self.b} = {self.a} {operator} {self.b}')

    def add(self):
        self.operation(self.a, self.b, '+')

    def subtract(self):
        self.operation(self.a, self.b, '-')

    def multiply(self):
        self.operation(self.a, self.b, '*')

    def divide(self):
        self.operation(self.a, self.b, '/')


if __name__ == '__main__':
    a1 = input('Argument 1:')
    a2 = input('Argument 2:')
    cn = ComplexNumber(a1, a2)
    cn.add()
    cn.subtract()
    cn.multiply()
    cn.divide()
