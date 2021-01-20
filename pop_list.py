# - Using the `pop` method try solving the challenge below.  The baseball_players list at the end should only contain `Altuve` and `Correa`.
baseball_players = ['Altuve', 'Bregman', 'Correa', 'Springer']


last_player = baseball_players.pop()
second_player = baseball_players.pop(1)

print(baseball_players)
print(last_player, second_player)
