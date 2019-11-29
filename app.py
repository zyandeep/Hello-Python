# full_name = "John Smith"
# age = 20
# is_new = True
# print(f"{full_name} is {age} years old")
# if is_new:
#     print(f"{full_name} is NEW")
# else:
#     print(f"{full_name} is OLD")
# name = input("Name? ")
# color = input("Color? ")
# print(f"{name} likes {color}")
# weight_lb = float(input("Weight in Pounds: "))
# weight_kg = weight_lb * 0.45359237
# print(f"{weight_kg} in KG")
# multi_line = """This is Line 1
# This is Line 2
# This is Line 3
# Thank You,
# Bob
# """
# print(multi_line)
# text = "This is a line of text"
# text = (1, 2, 3, 4)
# print(text[-4])
# text = "This is a line of text"
# x = text[:]
# print(text == x)
# print(text is x)
# print(text.replace(text[text.find("line") : 14], "piece"))
# print(text)
# import math
# print(math.factorial(abs(-4)))
# house_price = 1000000
# credit = True
# if credit:
#     down_payment = 10
# else:
#     down_payment = 20
# print(f"Total: ${house_price * (down_payment / 100)}")
# name = input("Enter name: ")
# lenth_name = len(name)
# if lenth_name < 3:
#     print("Must be > 3 chras. long")
# elif lenth_name > 50:
#     print("Must be < 50 chras. long")
# else:
#     print(f"{name} looks good")
# import my_module
# weight = float(input("Weight? "))
# unit = input("[L]bs or [K]g? ")
# if unit.upper() == "L":
#     print(f"You are {round(weight * my_module.POUND_TO_KG, 2)} kg")
# elif unit.upper() == "K":
#     print(f"You are {round(weight / my_module.POUND_TO_KG, 2)} pounds")
# else:
#     print("INVALD UNIT")
# CAR GAME #
# KEYWORDS: help, start, stop, quit
# game_started = True
# car_moving = False

# def print_help():
#     print("""
#     start => to start the car
#     stop => to stop the car
#     quit => to quit the game
#     """)

# def print_unknown():
#     print("I don't understand that")

# def quit_game():
#     global game_started
#     game_started = False

# def start_car():
#     global car_moving
#     if car_moving:
#         print("Car already started!")
#     else:
#         car_moving = True
#         print("Car started... Ready to go!")

# def stop_car():
#     global car_moving
#     if not car_moving:
#         print("Car already stopped!")
#     else:
#         car_moving = False
#         print("Car stopped")


# game_commands = {
#     "help": print_help, 
#     "start": start_car,
#     "stop": stop_car,
#     "quit": quit_game
# }

# # GAME BEGINS
# while game_started:
#     user_input = input(">").lower()

#     if user_input in game_commands:
#         game_commands[user_input]()
#     else:
#         print_unknown()
# else:
#     print("## THE END ##")
# total = 0
# # prices = [10, 20, 34, 21]
# for item in range(1, 21, 1):
#     total += item
# print(f"total: ${total}")
# print(f"sum = {(20 * (20 + 1)) / 2}")
# my_range = range(3)
# for x in my_range:
#     for y in my_range:
#         print((x, y))
# patterns = (2, 2, 2, 2, 7)

# for item in patterns:
#     # print("X" * item)
#     for i in range(item):
#         print("X", end="")    
#     print()
# str_input = input("Enter some numbers: ")
# str_list = str_input.split(sep=" ")

# res = float(str_list[0])

# for item in str_list:
#     if float(item) > res:
#         res = float(item)
# print(res)

# matrix = [
#     [1, 2, 3],
#     [4, 5],
#     [6, 9, 10]
# ]
# for row in matrix:
#     for item in row:
#         print(item, end=" ")

#     print()
# print(matrix[1][1])
# my_list = [12, 4, 5, 3, 4, 5, 3, 10]
# new_list = []
# for item in my_list:
#     if not item in new_list:
#         new_list.append(item)    
# print("new list: ", new_list)
# person = {
#     "name": "Bob",
#     "age": 23,
#     "is_alive": False
# }
# print(person.get("agee", 0))
# number_to_text = {
#     "0": "Zero",
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four",
#     "5": "Five",
#     "6": "Six",
#     "7": "Seven",
#     "8": "Eight",
#     "9": "Nine",
# }
# number_str = input("Enter a number: ")
# for item in number_str:
#     print(number_to_text.get(item, "UNKNOWN"), end=" ")


