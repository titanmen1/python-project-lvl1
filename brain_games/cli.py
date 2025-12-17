"""Prompt library usage example."""

import prompt

"""Идея, что в начале студент создаёт исполняемый файл brain-games и cli.py
для того, чтобы быстрее проверить работоспособность настроенного окружения.
Далее студент приступает к написанию игр и общей логики (движка).
cli.py и brain-games в итоге так и остаются висеть в проекте
и они не должны использоваться для игр, движка или ещё чего-то.
После создания brain-games и cli.py, далее об этих файлах можно забыть"""


def run():
    """Interact with user."""
    print('Welcome to the Brain Games!\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
