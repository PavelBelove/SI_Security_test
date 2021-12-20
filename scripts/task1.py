"""
The function calculates the minimum consumed energy
"""

IS_DEBUG = False
ACTION_ACCEPT = 'принять'
ACTION_UNLOAD = 'выгрузить'

# def analyse(programm: list[tuple[str, x]] → int
# Функция написанная по такой сигнатуре не получает данных о ящиках уже находящихся на складе.
# Проблемы возникнут при команде извлечь ящик, уже находившийся на конвейере
# Чтобы не использовать глобальных переменных, добавил опциональный аргумент
# def analyse(program: list[tuple[str, x]], klnvejer: list[int]) → int


def analyse(program, conveyor=[]):
    """The function calculates the minimum consumed energy

    : param program: list with tuples (command, mailbox number)
    : type list
    correct commands "принять" "выгрузить"

    : param conveyor:, defaults to 0
    : type list: List of box numbers on the conveyor (int)
    The argument is required if the program uses boxes that were previously on the conveyor.

    : rtype: int
    : return: Minimum energy required to run the program

     Examples:
     ---------
     >>> analyse([('принять', 1), ('выгрузить', 1)], [2, 3])
     2
     """

    energy = 0
    nums = [i[1] for i in program]
    conveyor_copy = conveyor[:]

    for i, comand in enumerate(program):
        if comand[0].lower() == ACTION_ACCEPT and comand[1] in nums[(i + 1):]:
            energy += 1
            conveyor_copy.append(comand[1])
            log(f'{energy}, {conveyor_copy}, Box {comand[1]} still needed')
        elif comand[0].lower() == ACTION_ACCEPT:
            energy += 1
            log(
                f'{energy}, {conveyor_copy}, Box {comand[1]} is no longer needed')
        elif comand[0].lower() == ACTION_UNLOAD:
            index = conveyor_copy.index(comand[1])
            energy += len(conveyor_copy[index:])
            new_program = [(ACTION_ACCEPT, i)
                           for i in conveyor_copy[index + 1:]] + program[i + 1:]
            conveyor_copy = conveyor_copy[:index]
            log(f'Unload {comand[1]} recursion {conveyor_copy}')
            energy += analyse(new_program, conveyor_copy)
            log(f'{energy}, {conveyor_copy}, Unload {comand[1]}')

            break

    return energy


def log(message):
    """prints if IS_DEBUG == True"""
    if IS_DEBUG:
        print(message)
