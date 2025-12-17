"""The "Prime" game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Понятие is_prime отделено от проверки на ввод пользователя.
# Функция-предикат возвращает булево значение.
def is_prime(number):
    """Return True if @number is Prime, otherwise return False."""
    # Пограничные случаи: 1, 0 и отрицательные числа
    if number <= 1:
        return False
    divisor = 2
    # Оптимизация: вводим ограничение при поиске делителей.
    while divisor <= number // 2:
        if not number % divisor:
            return False
        divisor += 1
    return True


def generate_round():
    """Generate data for the one round of "Prime game"."""
    question = randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return str(question), correct_answer
