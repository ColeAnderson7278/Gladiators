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
        for randint in range(attacker['Damage Low'], attacker['Damage High']):
            attack = randint
            defender['Health'] = defender['Health'] - attack
            attacker['Rage'] = attacker['Rage'] + 15
            return defender['Health']

    if attacker['Rage'] > 0:
        for randint in range(1, 100):
            if randint <= attacker['Rage']:
                for randint in range(attacker['Damage Low'],
                                     attacker['Damage High']):
                    attack = randint * 2
                    defender['Health'] = defender['Health'] - attack
                    attacker['Rage'] = 0
                    return defender['Health']

        else:
            for randint in range(attacker['Damage Low'],
                                 attacker['Damage High']):
                attack = randint
                defender['Health'] = defender['Health'] - attack
                attacker['Rage'] = attacker['Rage'] + 15
                return defender['Health']


def heal(gladiator):
    if gladiator['Rage'] >= 10:
        if gladiator['Health'] == 100:
            return None
        if gladiator['Health'] in range(96, 99):
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
