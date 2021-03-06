import time
import random


# player info
player = {
    'name': 'Hero',
    'lvl': 1,
    'xp': 0,
    'lvlNext': 25,
    'stats': {
        'Str': 1,
        'Def': 1,
        'Dex': 1,
        'Int': 1,
        'maxHp': 50, # Max Hp should increase with level
        "Atk": [7, 15], #Attack should also increase with level
    }
}



hero_path = ["Mage", "Wanderer", "Spirit Walker"]

# Enemy info

enemies = ["Imp", "Undead", "Mutant Wolf", "Corrupt Elf", "Enemy Soldier"]
randomEnemy = random.choice(enemies)

enemy = {
    'name': randomEnemy,
    'lvl': 1,
    'xp': 0,
    'reward': 25,
    'lvlNext': 25,
    'stats': {
        'Str': 1,
        'Def': 1,
        'Dex': 1,
        'Int': 1,
        'Hp': 50, #  Max Hp should increase with level
        "Atk": [5, 12], #Attack should also increase with level
    }
}

#leveling up 

def level(player):
    nStr, nDef, nDex, nInt = 0, 0, 0, 0
    while player['xp'] >= player['lvlNext']:
        player['lvl'] += 1
        player['xp'] = player['xp'] - player['lvlNext']
        player['lvlNext'] = round(player['lvlNext'] * 1.5)
        nStr += 1
        nDef += 1
        nDex += 1
        nInt += 1

    print('level:', player['lvl']) # current level
    print('STR {} +{} DEF {} +{} DEX {} +{} INT {} +{}'.format(player['stats']['Str'], nStr,
                                                               player['stats']['Def'], nDef,
                                                               player['stats']['Dex'], nDex,
                                                               player['stats']['Int'], nInt))
    print('To next level: {}%'.format(int(player['xp'] / player['lvlNext']) * 100)) # prints percentage to next level
    print('Next:', player['lvlNext']) 
    player['stats']['Str'] += nStr
    player['stats']['Def'] += nDef
    player['stats']['Dex'] += nDex
    player['stats']['Int'] += nInt

# Input response function 

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry I don't understand")
    return response




def play_game():
    companion = []
    items = []
    intro()
    ruskett_valley(items, player)

def print_pause(message):
    print(message)
    time.sleep(2)

def dialog(message):
    print(message)
    time.sleep(3)

def exit_cave(items):
    print_pause("You exit the cave.")

def enter():
    print_pause("You enter the cave.")

def exit():
    print("return to over world")# build overworld function 

def intro():
    print_pause("You wake in a forest with no memory of where you are or how you got there.")
    print_pause("You check your cell phone but no signal.")
    print_pause("Strange Voice: From what I've been told your not going to reach home with that thing!")
    print_pause("You jump up starteled thinking you were alone.")
    print_pause("You: Where am I? and Who are you? ")
    print_pause("Stranger: I'm Theadore but everyone calls me Ted.")
    print_pause("Ted: And as for your other question its getting dark soon we should get somewhere safe...")
    print_pause("Welcome to Ruskett Valley!")
    print_pause("You and Ted walk through the main road in the main village.")
    dialog("Ted: Ted explains that no one really knows where this place is"
    "we also don't know how everyone is arriving.")
    dialog("Me: so how do people survive and make a living here?")
    dialog("Ted explains the three hero paths.")

# Ruskett Valley Functions

def ruskett_valley(items): 
    print_pause("Welcome to ruskett.")
    ruskett_destinations(items)

def ruskett_destinations(items):
    print_pause("Where will you go?")
    response = input("Oak City\n"
                     "Magnolia Village\n"
                     "Tamarack City\n"
                     "Dogwood Village\n"
                     "Redwood City\n").lower()
    if "oak" in response:
        oak_city(items)
    elif "magnolia" in response:
        magnolia_village(items)
    elif "tamarack City" in response:
        tamarack_city(items)
    elif "dogwood" in response:
        dogwood_village(items)
    elif "redwood" in response:
        redwood_city(items)
    else:
        print_pause("Sorry I don't understand")
        ruskett_destinations(items)

def rusket_valley_local_vendors(items):
    print_pause("Where would you like to go?")
    response = input("Armory\n"
                    "Supply Store\n"
                    "Training Center\n"
                    "Traveller Registration\n").lower()
    if "armory" in response:
        ruskett_armory(items)
    elif "supply" in response:
        ruskett_supply(items)
    elif "training" in response:
        ruskett_training(items)
    elif 'traveller' in response:
        traveller_registraton(items)
    else:
        print_pause("Sorry I don't understand")

def ruskett_armory(items):
    print_pause("welcome")

def ruskett_supply(items):
    print_pause("Welcome")

def ruskett_training(itmes):
    print_pause("Welcome")

def traveller_registraton(items):
    print_pause("Welcome")

# Oak City Functions 

def oak_city(items): 
    print_pause("welcome to Oak City!")
    second_cave(items)

def second_cave(items):
    if 'armor' in items:
        enter()
        print_pause("The oasis is empty")
        exit_cave(items)
    else:
        enter()
        print_pause("A small oasis lies in the middle of the cave.")
        response = valid_input("In the oasis lies rusted armor, "
                               "what will you do?\n 1.pick up armor\n "
                               "2.exit cave\n", "pick up", "exit cave")
        if "pick up" in response:
            if 'dagger' in items:
                print_pause("The blue light dims")
                print_pause("As you don the armor a yellow mist swirls "
                            "around clearing the rust revealing shining"
                            "armor.")
                items.append("armor")
                exit_cave(items)
            else:
                items.append("armor")
                print_pause("The blue light dims.")
                exit_cave(items)
        elif "exit cave" in response:
            exit_cave(items)

# Magnolia Functions

def magnolia_village(items):
    print_pause("Welcome to Magnolia Village.")
    third_cave(items)

def third_cave(items):
    if 'medallion' in items:
        enter()
        print_pause("The giant oak sits in the dark cave"
                    " there is nothing to do here.")
        exit_cave(items)
    else:
        enter()
        response = valid_input("In the cave sits a large oak tree "
                               "As you get closer you see a glowing "
                               "medallion implanted in the tree,\n"
                               "what will you do?\n 1.Pick it up\n "
                               "2.exit cave\n", "pick up", "exit cave")
        if "pick up" in response:
            if 'armor' in items:
                print_pause("You grab the medallion")
                print_pause("The medallion glows and like a magnet fuses "
                            "to the center of your armor.")
                items.append("medallion")
                exit_cave(items)
            else:
                print_pause("As you reach for the medallion a burst "
                            "of energy throws you from the cave")

        elif "exit cave" in response:
            exit_cave(items)

# Dogwood Functions

def dogwood_village(items): 
    print_pause("Welcome to Dogwood Village.")

# Tamarack Functions

def tamarack_city(items): 
    print_pause("Welcome to Tamarack City")
    first_cave(items)

def first_cave(items):
    if 'dagger' in items:
        enter()
        print_pause("The alter sits empty in the dark room")
        exit_cave(items)
    else:
        enter()
        print_pause("In the center of the room stands a stone altar.")
        response = valid_input("In the middle of the altar lies a small dagger"
                               " and sheath what will you do?\n 1.pick up\n "
                               "2.exit cave.\n", "pick up", "exit cave")
        if "pick up" in response:
            print_pause("The yellow light dims.")
            items.append("dagger")
            print_pause("The cave shakes with a light rumble.")
            exit_cave(items)
        elif "exit cave" in response:
            exit_cave(items)

# Redwood Functions

def redwood_city(items):
    print_pause("Welcome to Redwood City.")
    fourth_cave(items)

def fourth_cave(items):
    print_pause("You enter the cave, it's light glows the brightest")
    response = valid_input("You see a door blocked by a shape shifter. "
                           "What will you do?\n 1.approach\n 2.exit cave\n",
                           "approach", "exit cave")
    if "exit cave" in response:
        print_pause("The shifter stares as you back out of the cave.")
    elif "approach" in response:
        print_pause("The shifter turns into a " + enemy + "!")
        print_pause("You must fight your way through.")
        # fight(items)
    else:
        print_pause("Sorry I don't understand")
        return response


#Fight

def takeDmg(attacker, defender):
    dmg = random.randint(attacker['stats']['Atk'][0], attacker['stats']['Atk'][1])
    defender['stats']['maxHp'] = defender['stats']['maxHp'] - dmg
    if defender['stats']['maxHp'] <= 0:
        print('{} has been slain'.format(defender['name']))
        player['xp'] = enemy['reward']
        level(player)
        exit() # exits the encounter once enemy is defeated
    else: 
        print('{} takes {} damage!'.format(defender['name'], dmg))


def commands(player, enemy): # add defense option 
    while True:
        print('--------------------')
        response = input('Do you want to attack? yes/no; ').lower()
        if 'yes' in response:
            takeDmg(player, enemy)
        elif 'no' in response:
            print('{} takes the opportunity to attack!').format(enemy['name'])
            takeDmg(enemy, player)
        else:
            pass

# def fight(items):
#     if 'medallion' in items:
#         print_pause("The items you found in the caves begin to glow")
#         fight_path()
#     else:
#         print_pause("You are not strong enough to fight.")
#         exit_cave(items)


# def fight_path():
#     print_pause("What will you do? Please enter a number:")
#     choice = input("1.Touch the medallion\n"
#                    "2.Grab the dagger\n"
#                    "3.Ready your armor\n")
#     if choice == '1':
#         print_pause("Your medallion  emits a bright green light.")
#         print_pause("The light Blinds your foe!")
#         print_pause("What will you do next? Please enter a number")
#         choice2 = input("1.Ready your armor\n"
#                         "2.Grab the dagger\n")
#         if choice2 == '1':
#             print_pause("your armor shifts slightly as if bracing itself.")
#             print_pause("the dagger glows and becomes a broadsword.")
#             print_pause("The magic from your medallion and armor swirl "
#                         " around infusing with your sword.")
#             print_pause("While your foe is blinded you attack!")
#             print_pause("With a few swift strikes you defeat your enemy.")
#             print_pause("The door behind him opens revealing a path "
#                         "to you bedroom.")
#             you_win()
#         elif choice2 == '2':
#             print_pause("the dagger glows but does nothing.")
#             print_pause("Your opponent laughs as he charges toward you.")
#             you_lose()
#         else:
#             print_pause("Sorry I don't understand.")
#             return choice2
#     elif choice == '2':
#         print_pause("The dagger glows but does nothing")
#         print_pause("Your opponent laughs as he charges toward you.")
#         you_lose()
#     elif choice == '3':
#         print_pause("Your armor shifts slightly as if bracing itself.")
#         print_pause("Your opponent attacks but get gets knocked back.")
#         print_pause("What will you do next? Please enter a number:")
#         choice3 = input("1.Touch the medallion\n"
#                         "2.Grab the dagger\n")
#         if choice3 == '1':
#             print_pause("Your medallion  emits a bright green light.")
#             print_pause("The light Blinds your foe!")
#             print_pause("the dagger glows and becomes a broadsword.")
#             print_pause("The magic from your medallion and armor swirl "
#                         " around infusing with your sword.")
#             print_pause("While your foe is blinded you attack!")
#             print_pause("With a few swift strikes you defeat your enemy.")
#             print_pause("The door behind him opens revealing a path "
#                         "to you bedroom.")
#             you_win()
#         elif choice3 == '2':
#             print_pause("The dagger glows but does nothing")
#             print_pause("Your opponent laughs as he charges toward you.")
#             you_lose()
#         else:
#             print_pause("Sorry I don't understand")
#             return choice3
#     else:
#         return choice





def play_again():
    response = valid_input("Would you like to play again?\n yes\n no\n",
                           "yes", "no")
    if "yes" in response:
        play_game()
    elif "no" in response:
        exit()


def you_win():
    print_pause("YOU WIN, CONGRATULATIONS!!")
    print_pause("GAME OVER")
    play_again()


def you_lose():
    print_pause("Your enemy unleashes a barrage of attacks!")
    print_pause("YOU DIED")
    print_pause("GAME OVER")
    play_again()


play_game()



