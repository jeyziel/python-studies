import random

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    damage = random.randrange(enemyatkl, enemyatkh)

    playerhp = playerhp - damage

    if playerhp <= 30 :
        playerhp = 30

    print("enemy strikes for ", damage,
    "points of damage. The current HP is ", playerhp)

    if playerhp > 30:
        continue
    
    print("you have low health. you've been teleported to the nearest inn.")
    break

    # if playerhp == 0:
    #     print("you have dead, you cannot respawn, as you are dead.")