import shell
import core


def begin():
    name = input(
        'You awaken to hot sand against your skin, the sun barring upon you, \nand a thousand voices shouting your name.\n\nWhat are they shouting? '
    )
    return name.capitalize()


def who_are_you(name):
    while True:
        choice = input(
            '\nAs your mind clears you begin to remember. What are you {}?\n\n>>> Berserker\nPros: High Attack and Rage \nCons: Chance To Graze and No Magic\n\n>>> Monk\nPros: High Health,Precision Attacks, and High Magic\nCons: Low Rage and Weak Attacks\n\n>>> Warrior\nPros: Well Rounded \nCons: No High Abilities\n\n>>> Jester\nPros: Chance To Kill In A Single Blow and Fair Magic \nCons: Very Weak Health and Low Rage\n'.
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
            print('\nChoose A Class {}!!!'.format(name.capitalize()))


def main():
    name = begin()
    who_are_you(name)


if __name__ == '__main__':
    main()
