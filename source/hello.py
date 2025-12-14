#!/usr/bin/env python3
"""CLI-приветствие с проверкой подключения к интернету."""

from typer import Option, run
from rich.console import Console
import requests

console = Console()

def main(
    name: str,
    lastname: str = Option("", "--lastname", "-l", help="Фамилия пользователя"),
    formal: bool = Option(False, "--formal", "-f", help="Формальное приветствие"),
    check_ip: bool = Option(False, "--check-ip", help="Показать внешний IP"),
) -> None:
    """Приветствует пользователя, опционально показывает внешний IP."""
    if formal:
        greeting = f"Добрый день, {name} {lastname}".strip() + "!"
    else:
        greeting = f"Привет, {name}!"

    console.print(f"[bold green]{greeting}[/bold green]")

    if check_ip:
        try:
            resp = requests.get("https://api.ipify.org?format=json", timeout=5)
            ip = resp.json().get("ip", "unknown")
            console.print(f"[dim]Ваш внешний IP: {ip}[/dim]")
        except requests.RequestException:
            console.print("[red]Не удалось определить IP[/red]")

if __name__ == "__main__":
    run(main)
