team1_name = 'Мастера кода'
team2_name = 'Волшебники данных'
# решил вводить числа с клавиатуры, ибо в целом ограничений никаких не было
team1_num = int(input('Количество игроков в команде 1: '))
team2_num = int(input('Количество игроков в команде 2: '))
score_1 = int(input('Счет команды 1: '))
score_2 = int(input('Счет команды 2: '))
team1_time = float(input('Время команды 1: '))
team2_time = float(input('Время команды 2: '))

task_total = score_1 + score_2
tima_avg = (team1_time + team2_time) / task_total

challenge_result = None
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды {}!'.format(team1_name)
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды {}!'.format(team2_name)
else:
    challenge_result = 'Ничья!'

# %
print('В команде %(team1_name)s участников: %(team1_num)d!')
print('В команде %(team2_name)s участников: %(team2_num)d!')
print('Итого сегодня в командах участников: %(team1_num)d и %(team2_num)d !')

# format
print('Команда {} решила задач: {} !'.format(team1_name, score_1))
print('Команда {} решила задач: {} !'.format(team2_name, score_2))
print('{} решили задачи за {} с !'.format(team1_name, team1_time))
print('{} решили задачи за {} с !'.format(team2_name, team2_time))

# f-string
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {task_total} задач, в среднем по {tima_avg} секунды на задачу!')