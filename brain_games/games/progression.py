"""The "Prograssion" game."""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10
MAX_INITIAL_VALUE = 20
MIN_STEP, MAX_STEP = -10, 10


def get_question(init_value, step, index_of_hole):
    question = ''
    counter = 0
    while counter < PROGRESSION_LENGTH:
        # Следим, чтобы в начало строки не попада лишний пробел.
        if counter > 0:
            question += ' '
        if counter == index_of_hole:
            question += '..'
        else:
            # Для вычисления значения любого члена арифметической прогрессии
            # удобно использовать формулу
            current_value = init_value + step * counter
            question += str(current_value)
        counter += 1
    return question


# Генерация данных в отдельной функции упрощает анализ кода.
def generate_round():
    """Generate data for the one round of "Progression game"."""
    init_value = randint(0, MAX_INITIAL_VALUE)
    step = randint(MIN_STEP, MAX_STEP)
    index_of_hole = randint(0, PROGRESSION_LENGTH - 1)

    question = get_question(init_value, step, index_of_hole)
    correct_answer = init_value + step * index_of_hole

    return question, str(correct_answer)
