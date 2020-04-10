class Circle:
    pi=3.14

    def __init__(self, radius):
        self.r=radius

    def area_of_circle(self):
        result=Circle.pi*self.r*self.r
        print(result)

c1=Circle(2)
c2=Circle(4)

c1.area_of_circle()
c2.area_of_circle()