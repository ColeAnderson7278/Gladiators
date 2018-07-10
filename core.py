from random import randint


def new_gladiator(health, rage, damage_low, damage_high, magic):
    return {
        'Health': health,
        'Rage': rage,
        'Damage Low': damage_low,
        'Damage High': damage_high,
        'Magic': magic
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


def is_dead(gladiator):
    if gladiator['Health'] <= 0:
        return True
    else:
        return False
