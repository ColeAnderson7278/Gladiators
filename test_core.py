from core import *


def test_new_gladiator():
    assert new_gladiator(55, 35, 5, 25, 10) == ({
        'Health': 55,
        'Rage': 35,
        'Damage Low': 5,
        'Damage High': 25,
        'Magic': 10
    })
    assert new_gladiator(100, 0, 5, 25, 5) == ({
        'Health': 100,
        'Rage': 0,
        'Damage Low': 5,
        'Damage High': 25,
        'Magic': 5
    })
    assert new_gladiator(0, 0, 0, 0, 0) == ({
        'Health': 0,
        'Rage': 0,
        'Damage Low': 0,
        'Damage High': 0,
        'Magic': 0
    })


def test_attack():
    attacker = {'Health': 100, 'Rage': 0, 'Damage Low': 5, 'Damage High': 25}
    defender = {'Health': 100, 'Rage': 0, 'Damage Low': 5, 'Damage High': 25}
    assert attack(attacker, defender) == defender['Health']

    attacker = {'Health': 55, 'Rage': 50, 'Damage Low': 5, 'Damage High': 25}
    defender = {'Health': 70, 'Rage': 10, 'Damage Low': 5, 'Damage High': 25}
    assert attack(attacker, defender) == defender['Health']


def test_heal():
    assert heal({
        'Health': 55,
        'Rage': 10,
        'Damage Low': 5,
        'Damage High': 25
    }) == ({
        'Health': 60,
        'Rage': 0,
        'Damage Low': 5,
        'Damage High': 25
    })
    assert heal({
        'Health': 100,
        'Rage': 0,
        'Damage Low': 5,
        'Damage High': 25
    }) == None
    assert heal({
        'Health': 97,
        'Rage': 20,
        'Damage Low': 5,
        'Damage High': 25
    }) == ({
        'Health': 100,
        'Rage': 10,
        'Damage Low': 5,
        'Damage High': 25
    })


def test_is_dead():
    assert is_dead({
        'Health': 0,
        'Rage': 0,
        'Damage Low': 5,
        'Damage High': 25
    }) == True
    assert is_dead({
        'Health': 100,
        'Rage': 0,
        'Damage Low': 5,
        'Damage High': 25
    }) == False


def test_cast():
    assert cast('Joe', {
        'Health': 100,
        'Rage': 0,
        'Damage Low': 5,
        'Damage High': 25,
        'Magic': 5
    }, 'Bill', {
        'Health': 100,
        'Rage': 0,
        'Damage Low': 5,
        'Damage High': 25,
        'Magic': 5
    }) == True

    assert cast('Joe', {
        'Health': 100,
        'Rage': 0,
        'Damage Low': 5,
        'Damage High': 25,
        'Magic': 0
    }, 'Bill', {
        'Health': 100,
        'Rage': 0,
        'Damage Low': 5,
        'Damage High': 25,
        'Magic': 0
    }) == None
