games = [input()for i in range(6)]
win = games.count('W')

if win == 6 or win == 5:
    print('1')
elif win == 3 or win == 4:
    print('2')
elif win == 2 or win == 1:
    print('3')
elif win == 0:
    print('-1')