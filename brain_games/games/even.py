"""The "Even" game."""

from random import randint

# Описание задается на уровне модуля (а не внутри функций),
# так проще видеть ключевые части игры.
# В описании не может быть перевода строки,
# описание не связано с выводом на экран.
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


# https://ru.hexlet.io/blog/posts/sovershennyy-kod-proektirovanie-funktsiy
def is_even(number):
    return number % 2 == 0


def generate_round():
    """Generate a question for the one game's round."""
    question = randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return str(question), correct_answer
