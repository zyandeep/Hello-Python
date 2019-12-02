# POUND_TO_KG = 0.453592
# from colorama import init, Fore, Style
# init()

# def display(msg, is_warning=False):
#     if is_warning:
#         print(Fore.RED + Style.BRIGHT + "THIS IS A WARNING!")
#         print(Style.RESET_ALL)

#     print(Fore.BLUE + msg)
#     print()

emojis_dict = {
    ":)": "😃",
    ":(": "😔",
    ":|": "😑",
    ";)": "😉",
    "|-O": "😴"
}

def get_emoji(word):
    # Using a VS CODE feature 
    
    return emojis_dict.get(word, word)
