import time
import random

player_victory = 0
enemy_victory = 0

for i in range(1, 4):
    time.sleep(2)  # Adding a noticeable time interval between rounds
    print('\n—————— This is round ' + str(i) + ' ——————')  # Round marker

    player_life = random.randint(100, 150)
    player_attack = random.randint(30, 50)
    enemy_life = random.randint(100, 150)
    enemy_attack = random.randint(30, 50)

    # Display the attributes of both characters
    print('【Player】\n' + 'Health: ' + str(player_life) + '\nAttack: ' + str(player_attack))
    print('------------------------')
    time.sleep(1)
    print('【Enemy】\n' + 'Health: ' + str(enemy_life) + '\nAttack: ' + str(enemy_attack))
    print('------------------------')
    time.sleep(1)

    # Both sides PK
    while player_life > 0 and enemy_life > 0:
        player_life = player_life - enemy_attack
        enemy_life = enemy_life - player_attack
        print('You attacked, 【Enemy】 remaining health: ' + str(enemy_life))
        print('Enemy attacked you, 【Player】 remaining health: ' + str(player_life))
        print('-----------------------')
        time.sleep(1.5)

    # Print the final result
    if player_life > 0 and enemy_life <= 0:
        player_victory += 1
        print('The enemy is dead, you won!')
    elif player_life <= 0 and enemy_life > 0:
        enemy_victory += 1
        print('Unfortunately, the enemy killed you!')
    else:
        print('Oh no, you and the enemy perished together!')

if player_victory > enemy_victory:
    time.sleep(1)
    print('【Final result: You won!】')
elif enemy_victory > player_victory:
    print('【Final result: You lost!】')
else:
    print('【Final result: It\'s a draw!】')
