# Сигнатура функции сохранена, но я не вижу смысла передавать n - по сути, это либо длина списка бонусов len(p), 
# либо ( при n < len(p)) достичь уровня больше n не возможно, что равнозначно списку p[:n],
# При n > len(p) и достаточно большом m возникает неопределенность.

def calculate(m, n, p):
    """Counts the maximum available bonus

    : param m: 
    : type int: number of days until the end of the promotion

    : param n:, defaults to 0 
    : type int:, number of days until the level is reset
    If n == 0, the length of the list 'p' is taken

    : param p:
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
    if n > len(p):
        raise IndexError('n should not be more len(p)')
    if n:
        p= p[:n]
    else:
        n = len(p)  
    for i in range(1, m+1):
        # reached the maximum level, we take the bonus and drop the level
        if level >= n: 
            bonuses += p[level-1]
            # print('Уровень достиг максимального', level, 'bonus', p[level-1])
            level = 1
        # there are few moves left until the end, press the button, collecting the remaining bonuses
        elif m-i <= len(p[level-1:]) and sum(p[:m-i]) < sum(p[-(m-i):]):
            bonuses += p[level-1]
            # print('Ходов мало. Жмем кнопку', level, 'bonus', p[level-1])
            level +=1  
        # profitable to press the button, press.
        elif sum(p[level-1:]) >= sum(p[:level-1]) or level == 1:
            bonuses += p[level-1]
            # print('Жмем кнопку', level, 'bonus', p[level-1])
            level +=1 
        # profitable to skip. skip and drop level
        elif sum(p[n-level:]) < sum(p[:n-level-1]) or sum(p[level-1:]) < sum(p[:level-1]):
            # print('Пропускаем ход', level, 'bonus', p[level-1])
            level = 1
              
    return bonuses


