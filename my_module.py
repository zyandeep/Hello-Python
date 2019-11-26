from colorama import init, Fore, Style
init()

def display(msg, is_warning=False):
    if is_warning:
        print(Fore.RED + Style.BRIGHT + "THIS IS A WARNING!")
        print(Style.RESET_ALL)

    print(Fore.BLUE + msg)
    print()
