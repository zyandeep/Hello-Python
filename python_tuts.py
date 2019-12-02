# from sys import argv
# print(len(argv))
# print(argv)
""" True => 1
False => 0 """

# if 0:
#     print("Hello")

# else:
#     print("Bye")
# i = j = 1
# while i <= 5:
#     print("Telusko", end=" ")

#     while j <= 5:
#         print("Rocks", end=" ")
#         j += 1
#     else:
#         j = 1
#         print()
#     i += 1
# for i in range(10, 1, -1):
#     print(i)
# for i in range(1, 21):
#     if i % 4 == 0:
#         continue
#     print(i, end=" ")
# for i in range(4, 0, -1):
#     for j in range(i):
#         print("#", end=" ")
#     print()
# class Car:
#     wheels = 4

#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     @classmethod
#     def get_wheels(cls):
#         return cls.wheels

#     def __str__(self):
#         return f"{self.wheels} {self.name} {self.color}"

#     def add_nums(self, *args, **kwargs):
#         print(args)
#         print(kwargs)
# c1 = Car("BMW", "red")
# c1.add_nums(1, 2, name="bob")
# print(c1)
# c2 = Car("Tesla", "blue")
# Car.wheels = 5
# print(c1.name, c1.wheels)
# print(c2.name, c2.wheels)
# print(Car.get_wheels())
# try:
#     print("Hello")
#     x = "bob"
# except:
#     pass
# print(x)
# class Parent:
#     def __init__(self, name):
#         self.name = name
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#     def __str__(self):
#         return f"{self.name}, {self.age}"
# c = Child("bob", 23)
# print(c)
# res = filter(lambda x: x % 2 == 0, range(10))
# print(list(res))

