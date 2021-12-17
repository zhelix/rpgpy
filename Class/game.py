import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,hp,mp,atk,df,magic):
        self.maxHP = hp
        self.HP = hp
        self.maxMP = mp
        self.MP = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df=df
        self.magic = magic
        self.action = ["Attack","Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl,self.atkh)

    def generate_spell(self,spell):
        mgl = self.magic[spell]["dmg"] - 5
        mgh = self.magic[spell]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self,dmg):
        self.HP -= dmg
        if self.HP <= 0:
            self.HP = 0
            return self.HP

    def get_HP(self):
        return self.HP

    def get_maxHP(self):
        return self.maxHP

    def get_MP(self):
        return self.MP

    def get_maxMP(self):
        return self.maxMP

    def reduce_MP(self,cost):
        self.MP -= cost

    def get_spell_name(self,spell):
        return self.magic[spell]["name"]

    def get_spell_mp_cost(self, spell):
        return self.magic[spell]["cost"]

    def choose_action(self):
        i=1
        print("Actions")
        for item in self.action:
            print(str(i) + ":", item)
            i += 1

    def choose_spell(self):
        i = 1
        print("Spells")
        for spell in self.magic:
            print(str(i) + "i:", spell["name"], "(cost:", str(spell["cost"])+ ")")
            i += 1