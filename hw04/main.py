class Ellipse(object):
    def __init__(self,a=0, b=0):
        self.a = a
        self.b = b

    def area(self):
        return 3.14*self.a*self.b

class Rectangle(object):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def area(self):
        return self.a*self.b

class Square(Rectangle):
    def __init__(self, a=0):
        super().__init__(a, a)


class Circle(Ellipse):
    def __init__(self, r=0):
        super().__init__(r, r)

    
def compute_area(n):
    max = len(n)-1
    s = 0
    for i in range(0, max+1):
        c = n[i]
        s = s + c.area()
    return s

shapes = [Ellipse(10, 20), Square(15), Circle(5),
          Rectangle(20, 15), Circle(5), Square(15),
          Ellipse(10, 20)]

total_area = compute_area(shapes)
print(total_area)
