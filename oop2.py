# from typing import Any


# class Banknote:
#     def __init__(self, value: int):
#         self.value = value

#     def __str__(self):
#         return f"Банкнота {self.value} сом"
    
    # def __repr__(self):
    #     return f"Banknote {self.value}"
    
#     def __eq__(self, object):
#         if object is None and not isinstance(object,Banknote):
#             return False
#         return self.value == object.value
    
#     def __ne__(self, object):
#         if object is None and not isinstance(object,Banknote):
#             return False
#         return self.value != object.value

#     def __lt__(self, object):
#         if object is None and not isinstance(object,Banknote):
#             return False
#         return self.value < object.value

#     def __gt__(self, object):
#         if object is None and not isinstance(object,Banknote):
#             return False
#         return self.value > object.value
    
#     def __le__(self, object):
#         if object is None and not isinstance(object,Banknote):
#             return False
#         return self.value <= object.value

#     def __ge__(self, object):
#         if object is None and not isinstance(object,Banknote):
#             return False
#         return self.value >= object.value


# b = Banknote(100)
# c = Banknote(100)
# print(b == c)
# print(b != c)
# print(b < c)
# print(b > c)
# print(b <= c)
# print(b >= c)

# class Wallet:

#     def __init__(self, *banknotes:Banknote):
#         self.container = []
#         self.container.extend(banknotes)
#         self.index = 0

#     def __str__(self):
#         return f"Wallet {self.container}"
    
#     def __contains__(self, item):
#         return item in self.container
    
#     def __bool__(self):
#         return len(self.container) > 0

#     def __len__(self):
#         return len(self.container)
    
#     def __call__(self):
#         return f"{sum(i for i in self.container)} сом"
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if 0 <= self.index < len(self.container):
#             value = self.container[self.index]
#             self.index += 1
#             return value
#         raise StopIteration
    
#     def __getitem__(self, item: int):
#         if item < 0 or item > len(self.container):
#             raise IndexError
#         return self.container[item]
    
#     def __setitem__(self, key: int, value: Banknote):
#         if key < 0 and key > len(self.container):
#             raise IndexError
#         self.container[key] = value

# b = Banknote(100)
# c = Banknote(100)
# w = Wallet(1000, 233, 345, 1234,567)
# if w: 
#     print("yes")
# else:
#     print("no")
# print(345 in w)
# print(len(w))
# for i in w:
#     print(i)
# print(w[4])
# w[0] = 1800
# print(w)

# class BaseClass:
#     def test(self):
#         print('BaseClass')

# class Mixin:
#     def testing(self):
#         print('Mixin')

# class MyClass(BaseClass, Mixin):
#     pass

# obj = MyClass()
# obj.testing()

# class Entity:
#     def __init__(self, pos_x, pos_y):
#         self.pos_x = pos_x
#         self.pos_y = pos_y

# class SquareMix:
#     def add_size(self, size_x):
#         self.size_x = size_x
#         self.size_y = size_x
    
#     def perimeter(self):
#         return self.size_x * 4
    
#     def square(self):
#         return self.size_x ** 2
    
# class SquareEntity(SquareMix, Entity):
#     pass

# square = SquareEntity(5, 4)
# square.add_size(500)
# print(square.size_x)
# print(square.size_y)
# print(square.square())
# print(square.perimeter())

# class Car:
#     def __init__(self, make, model, mileage):
#         self.__make = make
#         self.__model = model
#         self.mileage = mileage

#     def get_info(self):
#         return f"Car: {self.__make} {self.__model}, Mileage: {self.mileage}"

# car1 = Car("Infiniti", "QX60", 120000)
# print(car1.get_info()) 

# car1.__make = "Hyundai"
# car1.__model = "Sonata"
# print(car1.get_info()) 

# car1.mileage = 90000
# print(car1.get_info())  

# class AdditionMixin:
#     def add(self, second):
#         pass
 
# class MyClass(AdditionMixin):
#     def __init__(self, value):
#         self.value = value  
#    
#  def add(self, second):
#         return MyClass(self.value + second.value)

# obj1 = MyClass(5)
# obj2 = MyClass(10)
# res = obj1 + obj2
# print(res)



# class AdditionMixin:
#     def add(self):
#         pass

# class Car(AdditionMixin):
#     def __init__(self, __make, __model, __mileage):
#         self.__make = __make
#         self.__model = __model
#         self.__mileage = __mileage

#     def get_info(self):
#         return f"Машина: {self.__make} {self.__model}, Пробег: {self.__mileage}"

# car1 = Car("Toyota", "Prius", 160000)
# print(car1.get_info()) 

# car1.__make = "Hyundai"
# car1.__model = "Sonata"
# car1.__mileage = 90000
# print(car1.get_info()) 
  
# class UpperCaseMixin:
#     def to_uppercase(self):
#         return str(self).upper()

# class Text(UpperCaseMixin):
#     def __init__(self, text):
#         self.text = text
    
#     def __str__(self):
#         return self.text
    
# texting = Text("onepiece")
# print(texting.to_uppercase())

# class MultiplicationMixin:
#     def multiply(self, constant):
#         self.__constant = constant
#         return self * self.__constant

# class Con(MultiplicationMixin, int):
#     pass
    
# obj = Con(3)
# res = obj.multiply(15)
# print(res)
 

class CountDown:
    def __init__(self, start):
        self.count = start + 1
    def __iter__(self):
        return self
    def __next__(self):
        self.count-= 1
        if self.count < 0:
            raise StopIteration
        return self.count

def countdown(start):
    count = start + 1 
    while count > 0:
        yield count
        count -= 1

c = CountDown(5)
for i in c:
    print(i)

# counter = (i for i in range(5,-2,-2))
# for i in counter:
#     print(i)

