import shell
import core
from random import *


def begin():
    name = input(
        '\nYou awaken to hot sand against your skin, the sun bearing upon you, \nand a thousand voices shouting your name.\n\nWhat are they shouting? '
    )
    return name.capitalize().strip()


def who_are_you(name):
    while True:
        choice = input(
            '\n>>> 1) Berserker\nPros: High Attack and Rage \nCons: Chance To Graze and No Magic\n\n>>> 2) Monk\nPros: High Health,Precision Attacks, and High Magic\nCons: Low Rage and Weak Attacks\n\n>>> 3) Warrior\nPros: Well Rounded \nCons: No High Abilities\n\n>>> 4) Jester\nPros: Chance To Kill In A Single Blow and Fair Magic \nCons: Very Weak Health and Low Rage\n\nAs your mind clears you begin to remember your past. What are you {}?\n'.
            format(name.capitalize().strip()))
        if choice.lower() == '1':
            return core.new_gladiator(75, 50, 1, 51, 0)
        elif choice.lower() == '2':
            return core.new_gladiator(100, 0, 15, 15, 30)
        elif choice.lower() == '3':
            return core.new_gladiator(75, 15, 5, 31, 10)
        elif choice.lower() == '4':
            return core.new_gladiator(25, 0, 1, 101, 20)
        else:
            print('\nChoose A Class {}!!!'.format(name.capitalize().strip()))


def stat_printer(stats):
    print(
        '>>>Health: {}\n>>>Rage: {}\n>>>Damage Low: {}\n>>>Damage High: {}\n>>>Magic: {}\n'.
        format(stats['Health'], stats['Rage'], stats['Damage Low'],
               stats['Damage High'], stats['Magic']))


def enemy_spawner():
    print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    print(
        choice([
            '\nFocus warrior. They will come swift and strong.\n',
            '\nAnother obstacle stands in your path.\n',
            '\nNo time to waste! Fight or die!\n'
        ]))
    enemy_name = choice([
        'Bobby the Barb', 'Kyina the Relentless', 'Tim the Toolman',
        'Merciful Mort', 'Mega Buttercup', 'Tiappa the Dancer', 'Meat', 'Lobo'
    ])
    print('{} has entered the arena.'.format(enemy_name))
    enemy_stats = core.new_gladiator(
        randint(50, 100), randint(0, 30), randint(0, 15), randint(15, 50),
        randint(0, 30))
    stat_printer(enemy_stats)
    return enemy_name, enemy_stats


def check_the_dead(attacker, attacker_stats, defender, defender_stats):
    if core.is_dead(attacker_stats) == True:
        print('\n{} Is Victorious!!!'.format(defender))
        exit()
    if core.is_dead(defender_stats) == True:
        print('\n{} Is Victorious!!!'.format(attacker.capitalize().strip()))
        return True


def battle(attacker, attacker_stats, defender, defender_stats):
    if core.is_dead(attacker_stats) == True:
        print('\n{} Is Victorious!!!'.format(defender))
        exit()
    if core.is_dead(defender_stats) == True:
        return None
    else:
        while True:
            print('------------------------------------------------------')
            shell.display_stats(attacker, attacker_stats)
            shell.display_stats(defender, defender_stats)
            print('\n------------------------------------------------------')
            action = input(
                '\n{},what would you like to do?\n>>> 1) Attack(+15 Rage)\n>>> 2) Heal(-10 Rage, +10 Health)\n>>> 3) Cast(-10 Magic,-10 Enemy Health,+10 Health)\n>>> 4) Pass(+15 Magic)\n>>> 5) Quit\n'.
                format(attacker.capitalize().strip()))
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
                print('{} Is Victorious!!!'.format(defender))
                exit()
            else:
                print('\nIncorrect Input!!!')


def enemy_battle(enemy_name, enemy_stats, name, player_stats):
    if check_the_dead(name, player_stats, enemy_name, enemy_stats) == True:
        return True
    elif enemy_stats['Health'] < 50:
        if enemy_stats['Rage'] >= 10:
            core.heal(enemy_stats)
            print('\n{} healed himself.'.format(enemy_name))
        elif enemy_stats['Magic'] >= 10:
            core.cast(enemy_name, enemy_stats, name, player_stats)
            print('\n{} cast a spell upon you.'.format(enemy_name))
        else:
            core.attack(enemy_stats, player_stats)
            print('\n{} attacked you.'.format(enemy_name))
    else:
        if enemy_stats['Magic'] >= 10:
            core.cast(enemy_name, enemy_stats, name, player_stats)
            print('\n{} cast a spell upon you.'.format(enemy_name))
        else:
            core.attack(enemy_stats, player_stats)
            print('\n{} attacked you.'.format(enemy_name))


def rounds(name, player_stats, enemy_name, enemy_stats):
    while True:
        if battle(name, player_stats, enemy_name, enemy_stats) == True:
            enemy_name, enemy_stats = enemy_spawner()
            rounds(name, player_stats, enemy_name, enemy_stats)

        if enemy_battle(enemy_name, enemy_stats, name, player_stats) == True:
            enemy_name, enemy_stats = enemy_spawner()
            rounds(name, player_stats, enemy_name, enemy_stats)

        else:
            battle(name, player_stats, enemy_name, enemy_stats)
            enemy_battle(enemy_name, enemy_stats, name, player_stats)


def final():
    name = begin()
    player_stats = who_are_you(name)
    enemy_name, enemy_stats = enemy_spawner()
    rounds(name, player_stats, enemy_name, enemy_stats)


def main():
    final()


if __name__ == '__main__':
    main()
