import random
import time
import os
from rich import print
from rich.prompt import Prompt
from rich.spinner import Spinner
from rich.live import Live
from rich.columns import Columns

def ScreenClear():
    os.system("cls" if os.name == 'nt' else 'clear')

def CloseMenus():
    return False, False
    

MainMenu = True

while MainMenu:
    secret = random.randint(1, 100)

    guess = "no input"

    attempts = 0

    MenuCycle = True

    while MenuCycle:
        print("Guess number, from 1 to 100")

        try:
            print(f"Last input: {guess}")
            guess = int(input("\nType number up to 100: "))
        except ValueError:
            ScreenClear()
            print("Is not number! Type only number from 1 to 100")
            time.sleep(1.5)
            ScreenClear()
            
            continue

        attempts += 1

        if guess == secret:
            os.system("cls" if os.name == 'nt' else 'clear')
            print(f"You won! Secret number is: {secret}. You used {attempts} attempts!")
            retrychoise = Prompt.ask("Chose option 0=exit or 1=retry: ", default=1, choices=["0", "1"])

            if retrychoise == "1":
                ScreenClear()
                MenuCycle = False
                break
            elif retrychoise == "0":
                my_spinner = Columns(["[blue]Bye... ", Spinner("hearts")])
                with Live(my_spinner, refresh_per_second=8):
                    time.sleep(3)
                    MainMenu, MenuCycle = CloseMenus()
                    break

        HowNear = abs(guess - secret)

        if HowNear <= 3:
            ScreenClear()
            print("[red] 🔥 Holy hot!")

        elif HowNear <= 12:
            ScreenClear()
            print("[yellow] ☀️ Hot")

        elif HowNear <= 20:
            ScreenClear()
            print("[blue] ❄️ Cold")

        else:
            ScreenClear()
            print("[blue] 🧊 Very cold!")