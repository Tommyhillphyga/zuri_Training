class calculator ():
    def __init__(self, number1, number2) -> None:
        self.data1 = number1
        self.data2 = number2
    
    def __add__ (self):
        return self.data1 + self.data2
    
    def subtract (self):
        return self.data1 - self.data2

    def muitiply (self):
        return self.data * self.data2
    def modulus (self):
        return self.data1 % self.data2

cal = calculator(4,5)

print(cal.modulus())
print(cal.__add__())
