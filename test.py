from rich import print
from rich.panel import Panel
from rich.console import Group
from rich.columns import Columns
from rich.spinner import Spinner
import time

# 1. Збираємо кілька елементів у вертикальну групу
content = Group(
    "[bold white]Остання спроба:[/bold white] 45",
    "[yellow]Підказка:[/yellow] 🔥 Дуже гаряче!",
    "",  # Порожній рядок для відступу
    Columns(["[dim]Аналізуємо...[/dim]", Spinner("dots")])
)

# 2. Передаємо Group всередину Panel
game_card = Panel(
    content,
    title="[bold cyan]🎮 Ігровий статус[/bold cyan]",
    border_style="cyan",
    expand=False
)

game_card1 = Panel(
    "[bold yellow]penis",
    title="[bold yellow]🎮 Ігровий статус[/bold yellow]",
    border_style="black",
    expand=True
)

print(game_card, game_card1)
time.sleep(5)