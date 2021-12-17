from Class.game import Person, bcolors

magic = [{"name":"Firaga","cost":10,"dmg":600},
        {"name":"Thudaga","cost":10,"dmg":200},
         {"name": "Blizzaga", "cost": 10, "dmg": 100}]


Player = Person(780,65,55,34,magic)
Enemy = Person(1200,50,12,24,magic)

running = True
i=0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY APPEARS" + bcolors.ENDC)


while running:
    print("=====================")
    Player.choose_action()
    choice = input("Chose wisely ")
    index = int(choice) - 1
    if index == 0:
        dmg = Player.generate_damage()
        Enemy.take_damage(dmg)
        print("You've hit the enemy. DMG: ", dmg, "Enemy HP: ", Enemy.get_HP())

    if index == 1:
        Player.choose_spell()
        choice_mag = input("Chose magic wisely ")
        indexmag = int(choice_mag) -1
        print("you choice is ", Player.get_spell_name(int(indexmag)))
        print("Cast ", magic[indexmag]["name"], " did ", Player.generate_spell(indexmag), " damage")

    enemy_choice = 1
    enemy_dmg = Enemy.generate_damage()
    Player.take_damage(enemy_dmg)
    print("enemy attack us for ", enemy_dmg, "ponits. Current HP: ", Player.get_HP())
