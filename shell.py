import core
import single_player


def destroyer(incorrect, name):
    if incorrect == 5:
        print('STOP THAT AND CHOOSE!!!')
    if incorrect == 10:
        print('YOU DO NOT WANT THIS!!!')
    if incorrect >= 15:
        print(
            '{} Has Summoned Forth The Destroyer of Worlds to Fullfill His Blood Lust!!!'.
            format(name.strip().capitalize()))
        print(
            '\nThe arena, along with the gladiators, was destroyed in the mayhem and carnage that was unleashed... \n\nNo winners could be found.'
        )
        exit()


def classes(name):
    incorrect = 0
    while True:
        destroyer(incorrect, name)
        choice = input(
            '\n>>> 1) Berserker\nPros: High Attack and Rage \nCons: Chance To Graze and No Magic\n\n>>> 2) Monk\nPros: High Health,Precision Attacks, and High Magic\nCons: Low Rage and Weak Attacks\n\n>>> 3) Warrior\nPros: Well Rounded \nCons: No High Abilities\n\n>>> 4) Jester\nPros: Chance To Kill In A Single Blow and Fair Magic \nCons: Very Weak Health and Low Rage\n\nWhat class will you choose {}?\n'.
            format(name.strip().capitalize()))
        if choice.lower() == '1':
            return core.new_gladiator(75, 50, 1, 51, 0)
        elif choice.lower() == '2':
            return core.new_gladiator(100, 0, 15, 15, 30)
        elif choice.lower() == '3':
            return core.new_gladiator(75, 15, 5, 31, 10)
        elif choice.lower() == '4':
            return core.new_gladiator(25, 0, 1, 101, 20)
        else:
            incorrect = incorrect + 1
            print('\nChoose A Class {}!!!'.format(name.strip().capitalize()))


def intro():
    name_1 = input(
        '\nWelcome to the colosseum! Warrior one, what is your name? ')
    name_2 = input('\nWarrior two, what shall the crowds shout? ')
    stats_1 = classes(name_1)
    stats_2 = classes(name_2)
    return name_1, stats_1, name_2, stats_2


def display_stats(name, stats):
    print('\n>>> {} - Health:{} Rage:{} Magic:{}'.format(
        name.strip().capitalize(), stats['Health'], stats['Rage'],
        stats['Magic']))


def check_the_dead(attacker, attacker_stats, defender, defender_stats):
    if core.is_dead(attacker_stats) == True:
        print('\n{} Is Victorious!!!'.format(defender.strip().capitalize()))
        exit()
    if core.is_dead(defender_stats) == True:
        print('\n{} Is Victorious!!!'.format(attacker.strip().capitalize()))
        exit()


def battle(attacker, attacker_stats, defender, defender_stats):
    check_the_dead(attacker, attacker_stats, defender, defender_stats)
    while True:
        print('----------------------------------------')
        display_stats(attacker, attacker_stats)
        display_stats(defender, defender_stats)
        print('\n----------------------------------------')
        action = input(
            '\n{},what would you like to do?\n>>> 1) Attack(+15 Rage)\n>>> 2) Heal(-10 Rage,+10 Health)\n>>> 3) Cast(-10 Magic,-10 Enemy Health,+10 Health)\n>>> 4) Pass(+15)\n>>> 5) Quit\n'.
            format(attacker.strip().capitalize()))
        if action.lower() == '1':
            core.attack(attacker_stats, defender_stats)
            break
        if action.lower() == '2':
            if core.heal(attacker_stats) == None:
                print('\nYou Can Not Complete That Action!!!')
            else:
                core.heal(attacker_stats)
                break
        if action.lower() == '3':
            if core.cast(attacker, attacker_stats, defender,
                         defender_stats) == None:
                print('You Do Not Posses The Magic!!!')
            elif core.cast(attacker, attacker_stats, defender,
                           defender_stats) == True:
                break
        if action.lower() == '4':
            print('\nYou\'ve chosen to show mercy upon your enemy.\n')
            attacker_stats['Magic'] = attacker_stats['Magic'] + 15
            break
        if action.lower() == '5':
            print(
                '\nYou lay down your weapons and ask for mercy from your opponent.\n'
            )
            print('{} Is Victorious!!!'.format(defender.strip().capitalize()))
            exit()
        else:
            print('\nIncorrect Input!!!')


def single_multi():
    while True:
        print('Welcome to Gladiators!!!')
        choice = input(
            'Which gamemode do you choose?\n1) Single Player\n2) Two Player\n')
        if choice.lower() == '2':
            (name_1, stats_1, name_2, stats_2) = intro()
            while True:
                battle(name_1, stats_1, name_2, stats_2)
                battle(name_2, stats_2, name_1, stats_1)
        if choice.lower() == '1':
            single_player.final()
        else:
            print('\nIncorrect Response\n')


def main():
    single_multi()


if __name__ == '__main__':
    main()
