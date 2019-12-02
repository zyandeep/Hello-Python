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

def comma_joiner(word_list):
    for item in word_list:
        index = word_list.index(item)
        word_list[index] = str(item)
    
    return ",".join(word_list)
