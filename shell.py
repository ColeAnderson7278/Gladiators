import core


def destroyer(incorrect, name):
    if incorrect == 5:
        print('STOP THAT AND CHOOSE!!!')
    if incorrect == 10:
        print('YOU DO NOT WANT THIS!!!')
    if incorrect >= 15:
        print(
            '{} Has Summoned Forth The Destroyer of Worlds to Fullfill His Blood Lust!!!'.
            format(name.capitalize()))
        print(
            '\nThe arena, along with the gladiators, was destroyed in the mayham and carnage that was unleashed... \n\nNo winners could be found.'
        )
        exit()


def classes(name):
    incorrect = 0
    while True:
        destroyer(incorrect, name)
        choice = input(
            '\n>>> Berserker\nPros: High Attack and Rage \nCons: Chance To Graze and No Magic\n\n>>> Monk\nPros: High Health,Precision Attacks, and High Magic\nCons: Low Rage and Weak Attacks\n\n>>> Warrior\nPros: Well Rounded \nCons: No High Abilities\n\n>>> Jester\nPros: Chance To Kill In A Single Blow and Fair Magic \nCons: Very Weak Health and Low Rage\n\nWhat class will you choose {}?\n'.
            format(name.capitalize()))
        if choice.lower() == 'berserker':
            return core.new_gladiator(75, 50, 1, 51, 0)
        elif choice.lower() == 'monk':
            return core.new_gladiator(100, 0, 15, 15, 30)
        elif choice.lower() == 'warrior':
            return core.new_gladiator(75, 15, 5, 31, 10)
        elif choice.lower() == 'jester':
            return core.new_gladiator(25, 0, 1, 101, 20)
        else:
            incorrect = incorrect + 1
            print('\nChoose A Class {}!!!'.format(name.capitalize()))


def intro():
    name_1 = input(
        'Welcome to the colosseum! Warrior one, what is your name? ')
    name_2 = input('\nWarrior two, what shall the crowds shout? ')
    stats_1 = classes(name_1)
    stats_2 = classes(name_2)
    return name_1, stats_1, name_2, stats_2


def display_stats(name, stats):
    print('\n>>> {} - Health:{} Rage:{} Magic:{}'.format(
        name.capitalize(), stats['Health'], stats['Rage'], stats['Magic']))


def check_the_dead(attacker, attacker_stats, defender, defender_stats):
    if core.is_dead(attacker_stats) == True:
        print('\n{} Is Victorious!!!'.format(defender.capitalize()))
        exit()
    if core.is_dead(defender_stats) == True:
        print('\n{} Is Victorious!!!'.format(attacker.capitalize()))
        exit()


def battle(attacker, attacker_stats, defender, defender_stats):
    check_the_dead(attacker, attacker_stats, defender, defender_stats)
    while True:
        display_stats(attacker, attacker_stats)
        display_stats(defender, defender_stats)
        action = input(
            '\n{},what would you like to do?\n>>> Attack\n>>> Heal\n>>> Cast\n>>> Pass\n>>> Quit\n'.
            format(attacker.capitalize()))
        if action.lower() == 'attack':
            core.attack(attacker_stats, defender_stats)
            break
        if action.lower() == 'heal':
            if core.heal(attacker_stats) == None:
                print('\nYou Can Not Complete That Action!!!')
            else:
                core.heal(attacker_stats)
                break
        if action.lower() == 'cast':
            if core.cast(attacker, attacker_stats, defender,
                         defender_stats) == None:
                print('You Do Not Posses The Magic!!!')
            elif core.cast(attacker, attacker_stats, defender,
                           defender_stats) == True:
                break
        if action.lower() == 'pass':
            print('\nYou\'ve chosen to show mercy upon your enemy.\n')
            break
        if action.lower() == 'quit':
            print(
                '\nYou lay down your weapons and ask for mercy from your opponent.\n'
            )
            print('{} Is Victorious!!!'.format(defender.capitalize()))
            exit()
        else:
            print('\nIncorrect Input!!!')


def main():
    (name_1, stats_1, name_2, stats_2) = intro()
    while True:
        battle(name_1, stats_1, name_2, stats_2)
        battle(name_2, stats_2, name_1, stats_1)


if __name__ == '__main__':
    main()
