# text = "Madam"
# x = list(text)
# x.reverse()
# print("".join(x))
# for i in range(10):
#     print("Hello World!")
# x = {
#     "name": "Bob",
#     "age": 23,
#     "is_alive": True
# }
# # print(x.items())
# for k, v in x.items():
#     print(f"{k} => {v}")
# import my_pkg.my_module
# from my_pkg.my_module import comma_joiner
# print(
#     comma_joiner(["bob", "ram", True, 12.22])
# )
# import requests
# res = requests.get("https://www.google.co.in/")
# res.raise_for_status()
# print(res.status_code)
# print(res.text)
#! /home/emon/.local/share/virtualenvs/Intro_to_Python-ItUpX7On/bin/python
# import pyping
# r = pyping.ping("google.com")
# print(r)
# with open("./file.txt", "r") as file:
#     # for line in file.readlines():
#     #     print(line, end="")

#     print(
#         file.read()
#     )
# with open("./pic.jpeg", "rb") as sf,  open("copy_pic.jpeg", "wb") as df:
#     for byte_data in sf:
#         df.write(byte_data)
# for item in path.glob("**/*.py"):
#     print(item)
# path.mkdir()
# print(
#     path.absolute(),
#     # path.as_uri(),
# )
# import pathlib
# path = pathlib.Path("./.vscode")
# path.rmdir()

import sys

# READING FROM THE STDIN
text = sys.stdin.read()

# WRITING TO THE STDOUT
sys.stdout.write(text)
