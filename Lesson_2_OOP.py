#class MyObject:
#    int_field = 8
#    str_field = "a string"

#print(MyObject.int_field)
#print(MyObject.str_field)


#object1 = MyObject()
#object2 = MyObject()

#print(object1.int_field)
#print(object2.str_field)

#MyObject.int_field = 10
#print(MyObject.int_field)
#print(object1.int_field)

#object1.str_field = "another string"
#print(MyObject.str_field)
#print(object1.str_field)
#print(object2.str_field)

#*****************************************************************************************************************
#class Person:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age

#    def print_info(self):
#        print(self.name, "is", self.age)


#john = Person("John", 22)


#lucy = Person("Lucy", 21)


##Person.print_info(john)
##Person.print_info(lucy)
#john.print_info()
#lucy.print_info()

#*******************************************************************************************************************

#class MyObject:
#    class_attribute = 8

#    def __init__(self):
#       self.data_attribute = 42

#    def instance_method(self):
#        print(self.data_attribute)

#    @staticmethod
#    def static_method():
#        print(MyObject.class_attribute)

#if __name__ == "__main__":
#    MyObject.static_method()
#    obj = MyObject()
#    obj.instance_method()
#    obj.static_method()
    
#********************************************************************************************************************

#class Rectangle:
#    def __init__(self, side_a, side_b):
#        self.side_a = side_a
#        self.side_b = side_b

#    def __repr__(self):
#        return "Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)

#class Circle:
#    def __init__(self, radius):
#        self.radius = radius

#    def __repr__(self):
#        return "Circle(%.1f)" % self.radius

#    @classmethod
#    def from_rectagle(cls,rectangle):
#        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
#        return cls(radius)

#def main():
#    rectangle = Rectangle(3,4)
#    print(rectangle)
    
#    first_circle = Circle(1)
#    print(first_circle)

#    second_circle = Circle.from_rectagle(rectangle)
#    print(second_circle)

#if __name__ == "__main__":
#    main()

#*********************************************************************************************************************

                                                    #INCAPSULATION
                                                    # "name" public
                                                    # "_name" protected
                                                    # "__name" private
#*************************************************************************************************************************\
#class MyObject:
#    def __init__(self):
#        self.__attribute = 0

#    @property
#    def attribute(self):
#        return self.__attribute

#    @attribute.setter
#    def attribute(self, value):
#        if value < 100:
#            self.__attribute = value
 

#***************************************************************************************************************************

#class Complex:
#    def __init__(self, real = 0.0, im = 0.0):
#        self.real = real
#        self.im = im
        
#    def __repr__(self):
#        return "Complex({!r}, {!r})".format(self.real, self.im)
    
#    def __str__(self):
#        return "{}{:+}i".format(self.real, self.im)
    
#    def __add__(self, other):
#        return Complex(self.real+ other.real, self.im + other.im)

    
#    def __neg__(self):
#        return Complex(-self.real, -self.im)
                       
#    def __sub__(self, other):
#        return self + (-other)

#    def __eq__(self, other):
#        return self.real == other.real and self.im == other.im

#******************************************************************************************************************************

class MyObject:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == "secret" and self.password == "9ea)fc":
            return "Secret value"
        else:
            return object.__getattribute__(self, item)