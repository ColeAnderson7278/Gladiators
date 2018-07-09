import core


def intro():
    name_1 = input(
        'Welcome to the colosseum! Warrior one, what is your name? ')
    name_2 = input('\nWarrior two, what shall the crowds shout? ')
    stats_1 = core.new_gladiator(100, 0, 5, 25)
    stats_2 = core.new_gladiator(100, 0, 5, 25)
    print('{} - Health:{} Rage:{}'.format(name_1, stats_1['Health'],
                                          stats_1['Rage']))
    print('{} - Health:{} Rage:{}'.format(name_2, stats_2['Health'],
                                          stats_2['Rage']))


def main():
    intro()


if __name__ == '__main__':
    main()
