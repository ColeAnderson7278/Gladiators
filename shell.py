import core


def intro():
    name_1 = input(
        'Welcome to the colosseum! Warrior one, what is your name? ')
    name_2 = input('\nWarrior two, what shall the crowds shout? ')
    stats_1 = core.new_gladiator(100, 0, 100, 100)
    stats_2 = core.new_gladiator(100, 0, 5, 16)
    return name_1, stats_1, name_2, stats_2


def battle(attacker, attacker_stats, defender, defender_stats):
    if core.is_dead(attacker_stats) == True:
        winner(attacker, attacker_stats, defender, defender_stats)
    if core.is_dead(defender_stats) == True:
        winner(name_1, stats_1, name_2, stats_2)
    while True:
        print('\n{} - Health:{} Rage:{}'.format(attacker.capitalize(),
                                                attacker_stats['Health'],
                                                attacker_stats['Rage']))
        print('{} - Health:{} Rage:{}\n'.format(defender.capitalize(),
                                                defender_stats['Health'],
                                                defender_stats['Rage']))
        action = input(
            '{},what would you like to do?\n>>>Attack\n>>>Heal\n>>>Pass\n>>>Quit\n'.
            format(attacker.capitalize()))
        if action.lower() == 'attack':
            core.attack(attacker_stats, defender_stats)
            #print('{}\'s health is now at {}.\n'.format(
            #    defender.capitalize(), defender_stats['Health']))
            break
        if action.lower() == 'heal':
            core.heal(attacker_stats)
            #print('{}\'s health is now {}.\n'.format(attacker.capitalize(),
            #                                         attacker_stats['Health']))
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


def winner(name_1, stats_1, name_2, stats_2):
    if core.is_dead(stats_1) == True:
        print('\n{} Is Victorious!!!'.format(name_2.capitalize()))
        exit()
    if core.is_dead(stats_2) == True:
        print('\n{} Is Victorious!!!'.format(name_1.capitalize()))
        exit()


def main():
    (name_1, stats_1, name_2, stats_2) = intro()
    battle(name_1, stats_1, name_2, stats_2)
    battle(name_2, stats_2, name_1, stats_1)


if __name__ == '__main__':
    main()
