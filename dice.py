win = 1
lose = 0


def create(success, failure, probability):
    return {
        "success": success,
        "failure": failure,
        "probability": probability,
    }

def calculate(node):
    if node in [win, lose]:
        return node

    return node["probability"] * calculate(node["success"]) + (1 - node["probability"]) * calculate(node["failure"])

def simpleChain(nodes):
    if nodes == 0:
        return win
    return create(simpleChain(nodes - 1), lose, nodes/6)

def roundThree(howManyDiceLeft):
    if howManyDiceLeft == 0:
        return win
    return create(roundThree(howManyDiceLeft - 1), lose, howManyDiceLeft/6)

print("just round 3", calculate(roundThree(6)))

def roundTwo(howManyDiceLeftThisRound, howManyDifferentDiceRolled):
    if howManyDiceLeftThisRound == 0:
        return roundThree(6 - howManyDifferentDiceRolled)
    return create(
        roundTwo(howManyDiceLeftThisRound - 1, howManyDifferentDiceRolled + 1),
        roundTwo(howManyDiceLeftThisRound - 1, howManyDifferentDiceRolled),
        (6-howManyDifferentDiceRolled)/6)

def roundOne(howManyDiceLeftThisRound, howManyDifferentDiceRolled):
    if howManyDiceLeftThisRound == 0:
        return roundTwo(6 - howManyDifferentDiceRolled, howManyDifferentDiceRolled)
    return create(
        roundOne(howManyDiceLeftThisRound - 1, howManyDifferentDiceRolled + 1),
        roundOne(howManyDiceLeftThisRound - 1, howManyDifferentDiceRolled),
        (6-howManyDifferentDiceRolled)/6)

print("Full 3 rounds", calculate(roundOne(6, 0)))

for i in range(1,7):
    print(f'got {i} different on first roll', calculate(roundOne(0,i)))
