"""
Counts the maximum available bonus
"""

IS_DEBUG = False

# Сигнатура функции сохранена, но я не вижу смысла передавать n - по сути, это либо длина списка бонусов len(p),
# либо ( при n < len(p)) достичь уровня больше n не возможно, что равнозначно списку p[:n],
# При n > len(p) и достаточно большом m возникает неопределенность.


def calculate(days, levels, bonus_list):
    """
    Counts the maximum available bonus

    : param days:
    : type int: number of days until the end of the promotion

    : param levels:, defaults to 0
    : type int:, number of days until the level is reset
    If levels == 0, the length of the list 'p' is taken

    : param bonus_list:
    : type list:, list of bonuses depending on the player's level (int)

    : rtype: int
    : return: maximum available bonus

     Examples:
     ---------
     >>> calculate(3, 3, [6, 2, 1])
     12
    """

    level = 1
    bonuses = 0

    if levels > len(bonus_list):
        raise IndexError('levels should not be more len(bonus_list)')

    if levels:
        bonus_list = bonus_list[:levels]
    else:
        levels = len(bonus_list)

    for i in range(1, days + 1):
        few_moves_left = days - i <= len(bonus_list[level - 1:]) and sum(
            bonus_list[:days - i]) < sum(bonus_list[-(days - i):])
        profitable_to_take_a_bonus = sum(
            bonus_list[level - 1:]) >= sum(bonus_list[:level - 1]) or level == 1
        profitable_to_skip_the_day = sum(bonus_list[levels - level:]) < sum(
            bonus_list[:levels - level - 1]) \
            or sum(bonus_list[level - 1:]) < sum(bonus_list[:level - 1])

        if level >= levels:
            bonuses += bonus_list[level - 1]
            if IS_DEBUG:
                log(
                    f'Maximum level reached {level} bonus {bonus_list[level - 1]}')
            level = 1
        elif few_moves_left:
            bonuses += bonus_list[level - 1]
            if IS_DEBUG:
                log(
                    f'Days are few. Press the button {level} bonus {bonus_list[level - 1]}')
            level += 1
        elif profitable_to_take_a_bonus:
            bonuses += bonus_list[level - 1]
            if IS_DEBUG:
                log(f'Press the button {level} bonus {bonus_list[level - 1]}')
            level += 1
        elif profitable_to_skip_the_day:
            if IS_DEBUG:
                log(f'Skip the turn {level} bonus {bonus_list[level - 1]}')
            level = 1

    return bonuses


def log(message):
    """prints if IS_DEBUG == True"""
    if IS_DEBUG:
        print(message)
