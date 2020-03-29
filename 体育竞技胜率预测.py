import random

def printInfo():
    print("please enter the ability of player A and B (between 0 and 1)")

def getInputs():
    a = eval(input("player A"))
    b = eval(input("player B"))
    n = eval(input("how many times do you want to simulate?"))
    return a, b, n

def gameOver(scoreA,scoreB):
    return scoreA ==15 or scoreB ==15

def simOneGame(probA,probB):
    scoreA,scoreB = 0,0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving =="A":
            if random.random() < probA:
                scoreA +=1
            else:
                serving = "B"
        else:
            if random.random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA,scoreB

def simNGames(n, probA, probB):
    winsA, winsB = 0,0

    for i in range(n):
        scoreA, scoreB = simOneGame(probA,probB)
        if scoreA >scoreB :
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB


def printSummary(winsA, winsB):
    n = winsA +winsB
    print("we have test {} times".format(n))
    print("A wins {} times, and A's prob is {:0.1%}".format(winsA, winsA/n))
    print( "B wins {} times, and B's prob is {:0.1%}".format( winsB, winsB / n ) )


def main():
    printInfo()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

main()