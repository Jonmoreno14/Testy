import random


def level1():
    fractions = ["1/2", "1/3", "1/4", "1/5", "1/6", "1/7", "1/8", "1/9", "2/3"]
    num = random.randint(0, 9)
    return fractions[num]


def level2():
    fractions = ["1/16", "1/23", "1/6", "1/5", "1/6", "1/7", "1/8", "1/9", "2/3"]
    num = random.randint(0, 6)
    return fractions[num]


def level3():
    fractions = ["1/2", "1/3", "1/36", "1/42", "1/6", "1/7", "1/88", "1/9", "2/3"]
    num = random.randint(0, 6)
    return fractions[num]

