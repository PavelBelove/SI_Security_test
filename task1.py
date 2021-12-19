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
    nums = list([i[1] for i in program]) 
    conveyor = conveyor[:]
    for i, comand in enumerate(program):
        # print('')
        if comand[0].lower() == 'принять' and comand[1] in nums[(i+1):]: # the box is still needed, at the end
            energy += 1
            conveyor.append(comand[1])
            # print(energy, conveyor, f'ящик {comand[1]} еще нужен')
        elif comand[0].lower() == 'принять': #ящик сегодня не нужен, в начало
            energy += 1 
            # print(energy, conveyor, f'ящик {comand[1]} больше не нужен')
        elif comand[0].lower() == 'выгрузить':
            ind = conveyor.index(comand[1]) # entry guaranteed by condition
            energy += len(conveyor[ind:])
            new_program = [('принять', i) for i in conveyor[ind+1:]] + program[i+1:] # i-th box is not included
            conveyor = conveyor[:ind]
            # print(f'выгружаем {comand[1]} рекурсия {conveyor}')
            energy += analyse(new_program, conveyor) 
            # print(energy, conveyor, f'выгрузка {comand[1]}')
            break 
            
    return energy




