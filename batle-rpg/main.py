from classes.game import Person, bgcolor

magic = [
    {"name":"fire", "cost":10, "dmg":60},
    {"name": "thunder", "cost":10, "dmg":80},
    {"name":"blizzard", "cost":20, "dmg":60}
]

player = Person(460, 65, 60, 34, magic)

print(player.generate_damage())
print(player.generate_spell_damage(1))