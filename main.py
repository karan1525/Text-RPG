from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create Black Magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

# Create white magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White") # FINAL FANTASY!

# Create some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/ MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores party's HP/ MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [potion, hipotion, superpotion, elixer, hielixer, grenade]

player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("======================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index is 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for: ", dmg, "points of damage.")
    elif index is 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1

        if magic_choice is -1: # go back a step (0 basically)
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.spell_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough magic points" + bcolors.ENDC)
            continue

        # item = player.choose_item()
        # if item.type is "potion":
        #     player.heal(item.prop)
        #     print(bcolors.OKGREEN + "\n" + item.name + "heals for " + str(item.prop), "HP" + bcolors.ENDC)

        player.reduce_mp(spell.cost)

        if spell.type is "White":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for: ", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type is "Black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), " points of damage" + bcolors.ENDC + "\n")

    elif index is 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1

        if item_choice is -1:
            continue


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for: ", enemy_dmg)

    print("------------------------------")
    print("Enemy HP: " , bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC + "\n")
    print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

    if enemy.get_hp() is 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() is 0:
        print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
        running = False


