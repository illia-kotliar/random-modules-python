import random
import time
import os
from rich import print
from rich.prompt import Prompt
from rich.spinner import Spinner
from rich.live import Live
from rich.columns import Columns
from rich.console import Group
from rich.panel import Panel
from rich.align import Align
from rich.console import Console




def ScreenClear():
    os.system("cls" if os.name == 'nt' else 'clear')

def CloseMenus():
    return False, False




my_spinner = Columns(["[bold cyan]Bye... ", Spinner("hearts")])

SpinnerBye = Panel(
    Align.center(my_spinner),
    border_style="cyan",
    expand=True
)


NearNoInput = Panel(
    "[bold]💭 Wait for input...",
    title="[bold]Near status",
    border_style="white",
    expand=False
)
NearHolyHot = Panel(
    "[bold red]🔥 Holy hot!",
    title="[bold red]Near status",
    border_style="red",
    expand=False
)
NearHot = Panel(
    "[bold yellow]🌞 Hot",
    title="[bold yellow]Near status",
    border_style="yellow",
    expand=False
)
NearCold = Panel(
    "[bold blue]🐧 Cold",
    title="[bold blue]Near status",
    border_style="blue",
    expand=False
)
NearVeryCold = Panel(
    "[bold blue]🧊 Very cold!",
    title="[bold blue]Near status",
    border_style="blue",
    expand=False
)




console = Console()

MainMenu = True

attempts = 0

guess = "no input"

NearStatus = NearNoInput

while MainMenu:
    secret = random.randint(1, 100)

    MenuCycle = True

    while MenuCycle:




        MenuCycleGroup = Group(
            "[bold]Guess number from 1 to 100",
            f"[bold]Last input: {guess}"
            )
        MenuCyclePanel = Panel(
            MenuCycleGroup,
            title="[bold cyan]Game details",
            border_style="cyan",
            expand=False
            )

        


        print(NearStatus)

        try:
            print(MenuCyclePanel)
            guess = int(console.input("\n[bold]Type number up to 100: "))
        except ValueError:
            ScreenClear()
            print("[bold red]Is not number! Type only number from 1 to 100")
            time.sleep(1)
            ScreenClear()
            
            continue

        attempts += 1

        if guess == secret:
            os.system("cls" if os.name == 'nt' else 'clear')




            WinnerMenu = Panel(
                f"[bold #7DCEFF]You won! Secret number is: {secret}. You used {attempts} attempts!",
                title="[bold #FFF200]🏆 You winner!",
                border_style="#406C85",
                expand=False
                )


            

            print(WinnerMenu)
            retrychoise = Prompt.ask("Chose option 0=exit or 1=retry: ", default=1, choices=["0", "1"])

            if retrychoise == "1":
                NearStatus = NearNoInput
                ScreenClear()
                MenuCycle = False
                break
            elif retrychoise == "0":
                ScreenClear()
                with Live(SpinnerBye, refresh_per_second=8):
                    time.sleep(3)
                    MainMenu, MenuCycle = CloseMenus()
                    break

        HowNear = abs(guess - secret)

        if HowNear <= 3:
            ScreenClear()
            NearStatus = NearHolyHot

        elif HowNear <= 12:
            ScreenClear()
            NearStatus = NearHot

        elif HowNear <= 20:
            ScreenClear()
            NearStatus = NearCold

        else:
            ScreenClear()
            NearStatus = NearVeryCold