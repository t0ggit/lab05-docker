#!/usr/bin/env python3
"""
Простое CLI-приветствие с поддержкой фамилии и формального стиля.
"""

from typer import Option, run


def main(
    name: str,
    lastname: str = Option("", "--lastname", "-l", help="Фамилия пользователя"),
    formal: bool = Option(False, "--formal", "-f", help="Формальное приветствие"),
) -> None:
    """Приветствует пользователя по имени, опционально с фамилией и в формальном стиле."""
    if formal:
        greeting = f"Добрый день, {name} {lastname}".strip() + "!"
    else:
        greeting = f"Привет, {name}!"

    print(greeting)


if __name__ == "__main__":
    run(main) # через typer, чтобы самим не реализовавыть механику выбора опций
