#abstract classes can be considered as blue print for other classes. abstract classes have methods which are just defined and not declared
#abstract classes are used when you dont want to create object of a particular class, for example, great apes(having feature of moving), there cannot be direct objects for 'great apes', however we can have 'humans' as a class inherited from 'great apes' and have the definition of moving within 'human' class, also we can have 'lion' as a class inherited from 'great apes' and have the definition of moving within the 'lion' class

#Since python doesnot have built-in abstract feature, so to define a class as abstract import 'ABC' class from 'abc' package (from abc import ABC, abstractmethod), to make a method 'abstract' add a decorator(@abstractmethod) before the method within abstract class

from abc import ABC, abstractmethod
class Flower(ABC):
    @abstractmethod
    def petals(self):
        pass

class Rose(Flower):
    def petals(self):
        print("Rose has many petals and are red in color")

class Sunflower(Flower):
    def petals(self):
        print("Sunflower has five petals and are yellow in color")

class Shoeflower(Flower):
    def petals(self):
        print("Shoeflower has six petal and are pink in color")

sh1=Shoeflower()
sh1.petals()

s1=Sunflower()
s1.petals()

r1=Rose()
r1.petals()

# https://www.netjstech.com/2019/06/abstraction-in-python.html
