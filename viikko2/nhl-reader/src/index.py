import re
import requests
from rich.live import Live
from rich.table import Table
from rich.align import Align
from rich.console import Console
from rich.prompt import Prompt
from rich.padding import Padding
from player_reader import PlayerReader
from player_stats import PlayerStats


def main():# pylint: disable=too-many-statements
    console = Console()
    baseurl = "https://studies.cs.helsinki.fi/nhlstats/"
    response = requests.get(baseurl, timeout=10)
    seasons = re.findall(r"\b\d{4}-\d{2}\b", response.text)

    while True:
        season = Prompt.ask(
            f"[grey69]Seasons [magenta][{'/'.join(seasons)}][/magenta][cyan]()[/cyan][/grey69]"
        )

        if season.upper() == "Q":
            break

        if season not in seasons:
            console.print("[red]season does not exist in dataset[/red]")
            continue

        url = baseurl + f"{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)

        console.print(
            f"[grey69]Seasons [magenta][{'/'.join(seasons)}][/magenta][cyan]({season})[/cyan]:[/grey69]"
        )

        nationality_loop(stats, reader, console, season)


def nationality_loop(stats, reader, console, season):
    while True:
        nationalities = reader.get_nationalities()
        nationality = Prompt.ask(
            f"[grey69]Nationality [magenta][{'/'.join(nationalities)}][/magenta][cyan]()[/cyan][/grey69]"
        ).upper()

        if nationality == "Q":
            break

        if nationality not in nationalities:
            console.print("[red]nationality does not exist in dataset[/red]")
            continue

        players_table(stats, nationality, console, season)


def players_table(stats, nationality, console, season):# pylint: disable=too-many-state
    table = Table(show_footer=False)
    table_left = Align.left(table)

    with Live(table_left, console=console, screen=False):
        table.add_column("Released", style="cyan", no_wrap=True)
        table.add_column("teams", style="magenta")
        table.add_column("goals", style="green")
        table.add_column("assists", style="green")
        table.add_column("points", style="green")
        players = stats.top_scorers_by_nationality(nationality)
        subheader = f"[grey69][italic]Season {season} players from {nationality}[/italic][/grey69]"
        console.print(Padding(subheader, (0, 0, 0, 15)))
        for p in players:
            table.add_row(p.name, p.teams, str(p.goals), str(p.assists), str(p.points))


if __name__ == "__main__":
    main()
