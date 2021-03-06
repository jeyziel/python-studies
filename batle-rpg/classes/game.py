import random

class bgcolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.mp = mp
        self.maxmp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['attack', 'magic']

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)
    
    def take_damage(self, dmg):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def get_hp(self):
        return self.hp

    def get_max_hp(self.hp):
        return self.maxhp

    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp
    
    def reduce_mp(self, cost):
        self.mp -= cost
        return self.mp
    
    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_cost(self, i):
        return self.magic[i]["cost"]

    def choose_actions(self):
        i = 1
        print("ACTIONS")
        for action in self.actions:
            print(str(i) + ':', action)
            i += 1
    
    def choose_magic(spell):
        i = 1
        print("Magics")
        for spell in self.magic:
            print(str(i) + ':',spell["name"],
            "(cost :", str(spell["mp"]) + ')')
            i += 1