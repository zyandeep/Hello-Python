# print("Hello World!")
# name = input("Please enter name: ")
# age = input("Age? ")
# print(
#   f"Hello, { name.capitalize() }. You're { age } years old"
# )
# print("hello \nWorld!")
# print("world")
# x = 12 / 0
# print(x)
# text = "the Dog IS named Sammy"
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.count("d"))

# first_name = input("First name? ")
# last_name = input("Last name? ")
# print("Hello " + first_name.capitalize() + " " + last_name.capitalize())
# print(
#   "Hello, {} {}".format(first_name.capitalize(), last_name.capitalize())
# )
# print(
#   f"Hello, {first_name.capitalize()} {last_name.capitalize()}"
# )
# pi = 3.14159
# print("pi = " + str(pi))
# first_number = input("First Number? ")
# second_number = input("Second Number? ")
# print(int(first_number) / int(second_number))
# print(float(first_number) ** int(second_number))
# from datetime import datetime, timedelta
# cur_date = datetime.today()
# one_day = timedelta(weeks=1)
# print("Today is: " + str(datetime.now()))
# print(f"Today is: {  datetime.today() }")
# print(cur_date.year)
# print(cur_date.month)
# print(cur_date.day)
# print(cur_date.date())
# print(f"A week: { cur_date - one_day }")
# date_string = input("When's your birthday? (<weekday> dd-MON-YYYY HH:MM AM/PM): ")
# birth_day = datetime.strptime(date_string, "%a %d-%b-%Y %I:%M %p")
# print(f"Your birth day {birth_day}")
# print(f"Before that day {birth_day - one_day}")
# x = 23
# y = 0
# try:
#   print(x / y)
# except ZeroDivisionError as e:
#   print(f"Error { e }")
# else:
#   print("unknown error")  
# finally:
#   print("clean up code")
#   print()
# price = input("How much? ")
# price = float(price)
# tax = 0.0

# if price >= 10:
#     tax = 0.07

# print(f"total: {price - tax}")

amount = input("Enter amount: ")
amount = float(amount)
tax = 0.0

country = input("Enter country: ")
if country.lower() == "canada":
    state = input("Enter state: ")

    # if state.lower() == "alberta" or state.lower() == "nunavut" or state.lower() == "yukon":
    #     tax = 0.05
    if state.lower() in ("alberta", "nunavut", "yukon"):
        tax = 0.05
    elif state.lower() == "ontario":
        tax = 0.13
    else:
        tax = 0.15
    print(f"tax = { tax }, total = { amount + tax }")
    
else:
    print(f"tax = { tax }, total = { amount }")

