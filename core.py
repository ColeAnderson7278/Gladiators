from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    return {
        'Health': health,
        'Rage': rage,
        'Damage Low': damage_low,
        'Damage High': damage_high
    }


def attack(attacker, defender):
    if attacker['Rage'] == 0:
        defender['Health'] = defender['Health'] - randint(
            attacker['Damage Low'], attacker['Damage High'])
        attacker['Rage'] = attacker['Rage'] + 15
        return defender['Health']

    if attacker['Rage'] > 0:
        if randint(1, 100) <= attacker['Rage']:
            defender['Health'] = defender['Health'] - (
                randint(attacker['Damage Low'], attacker['Damage High']) * 2)
            attacker['Rage'] = 0
            print('\nCritical Hit!!!')
            return defender['Health']

        else:
            defender['Health'] = defender['Health'] - randint(
                attacker['Damage Low'], attacker['Damage High'])
            attacker['Rage'] = attacker['Rage'] + 15
            return defender['Health']


def heal(gladiator):
    if gladiator['Rage'] >= 10:
        if gladiator['Health'] == 100:
            return None
        if gladiator['Health'] in range(96, 100):
            gladiator['Rage'] = gladiator['Rage'] - 10
            gladiator['Health'] = 100
            return gladiator
        if gladiator['Health'] <= 95:
            gladiator['Rage'] = gladiator['Rage'] - 10
            gladiator['Health'] = gladiator['Health'] + 5
            return gladiator
    else:
        return None


def gladiator_classes(choice):
    if choice.lower() == 'berserker':
        return new_gladiator(65, 50, 1, 51)
    elif choice.lower() == 'monk':
        return new_gladiator(100, 0, 15, 15)
    elif choice.lower() == 'warrior':
        return new_gladiator(75, 15, 5, 31)
    elif choice.lower() == 'jester':
        return new_gladiator(25, 0, 1, 101)
    else:
        incorrect = incorrect + 1
        print('\nChoose A Class {}!!!'.format(name.capitalize()))


def is_dead(gladiator):
    if gladiator['Health'] <= 0:
        return True
    else:
        return False
