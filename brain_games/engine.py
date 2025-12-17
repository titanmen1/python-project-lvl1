"""The game engine."""

import prompt

ROUNDS_COUNT = 3


# Общая логика игр.
# Отвечает за взаимодействие с пользователем и игровой процесс (алгоритм).
# Она ничего не знает про конкретные игры.
# Знает лишь про понятия "описание" и "вопрос" с "ответом",
# которые предоставляет игра.
def run(game):
    """Run a game defined in game module."""
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print(f'Hello, {name}')

    print(game.DESCRIPTION)
    count = ROUNDS_COUNT
    while count:
        # Дестракчеринг – опция
        question, correct_answer = game.generate_round()

        print('Question:', question)
        answer = prompt.string('Your answer: ')

        if answer != correct_answer:
            print(
                f'{answer} is wrong answer ;(. '
                f'Correct answer was {correct_answer}.',
            )
            print(f"Let's try again, {name}!")
            return

        print('Correct!')
        count -= 1

    print(f'Congratulations, {name}!')
