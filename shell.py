import core


def intro():
    name_1 = input(
        'Welcome to the colosseum! Warrior one, what is your name? ')
    name_2 = input('\nWarrior two, what shall the crowds shout? ')
    stats_1 = core.new_gladiator(100, 0, 5, 16)
    stats_2 = core.new_gladiator(100, 0, 5, 16)
    return name_1, stats_1, name_2, stats_2


def display_stats(name, stats):
    print('\n>>> {} - Health:{} Rage:{}'.format(
        name.capitalize(), stats['Health'], stats['Rage']))


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
            '\n{},what would you like to do?\n>>> Attack\n>>> Heal\n>>> Pass\n>>> Quit\n'.
            format(attacker.capitalize()))
        if action.lower() == 'attack':
            core.attack(attacker_stats, defender_stats)
            break
        if action.lower() == 'heal':
            core.heal(attacker_stats)
            break
        if action.lower() == 'pass':
            print('You\'ve chosen to show mercy upon your enemy.\n')
            break
        if action.lower() == 'quit':
            print(
                'You lay down your weapons and ask for mercy from your opponent.\n'
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
