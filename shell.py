import core


def intro():
    name_1 = input(
        'Welcome to the colosseum! Warrior one, what is your name? ')
    name_1 = name_1.capitalize()
    name_2 = input('\nWarrior two, what shall the crowds shout? ')
    name_2 = name_2.capitalize()
    stats_1 = core.new_gladiator(100, 0, 5, 25)
    stats_2 = core.new_gladiator(100, 0, 5, 25)
    print('{} - Health:{} Rage:{}'.format(name_1, stats_1['Health'],
                                          stats_1['Rage']))
    print('{} - Health:{} Rage:{}\n'.format(name_2, stats_2['Health'],
                                            stats_2['Rage']))
    return name_1, stats_1, name_2, stats_2


def battle(name_1, stats_1, name_2, stats_2):
    action = input(
        '{},what would you like to do?\n>>>Attack\n>>>Heal\n>>>Pass\n>>>Quit\n'.
        format(name_1))
    if action.lower() == 'attack':
        core.attack(stats_1, stats_2)
        print('{}\'s health is now at {}'.format(name_2, stats_2['Health']))
    if action.lower == 'heal':
        
def main():
    (name_1, stats_1, name_2, stats_2) = intro()
    battle(name_1, stats_1, name_2, stats_2)


if __name__ == '__main__':
    main()
