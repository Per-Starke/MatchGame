__author__ = 'Per'

from Match_class import Match
from Player_class import Player
import random

numberOfPlayers = input("how many players? ")



def defineListOfPlayers():

    listOfPlayers = []

    for i in range (0, numberOfPlayers):
        playerName = raw_input("Player name: ")
        matchToAssingToPlayer = Match(i)
        player_i = Player(playerName, i, matchToAssingToPlayer)
        listOfPlayers.append(player_i)

    return listOfPlayers

def defineListOfMatches(listOfPlayers):

    listOfMatches = []

    for player in listOfPlayers:
        match = player.getAssignedMatch()
        listOfMatches.append(match)

    return listOfMatches

def assignLengthToMatches(listOfMatches, nrOfLongMatches):
    for match in listOfMatches:
        match.Length = False
    for i in range (0, nrOfLongMatches):
        listOfMatches[i].Length = True
    return listOfMatches


def shuffleListOfMatchesAndAssignToPlayers(listOfMatches, listOfPlayers):
    random.shuffle(listOfMatches)
    i = 0
    for match in listOfMatches:
        listOfPlayers[i].AssignedMatch = match
        i += 1

def assignVictory(listOfPlayers):
    listOfWinners = []
    for player in listOfPlayers:
        if player.AssignedMatch.getLength() == True:
            player.Victory = True
            listOfWinners.append(player)
        else:
            player.Victory = False
    return listOfWinners

def printWinners(listOfWinners):
    for winner in listOfWinners:
        print("")
        print("One Winner is '" + winner.getName() + "' with the player-number " + str(winner.getNumber()))
        print("")

listOfPlayers = defineListOfPlayers()

listOfMatches = defineListOfMatches(listOfPlayers)

nrOfWinners = input("Nr of winners: ")
listOfMatches = assignLengthToMatches(listOfMatches, nrOfWinners)

shuffleListOfMatchesAndAssignToPlayers(listOfMatches, listOfPlayers)

listOfWinners = assignVictory(listOfPlayers)

printWinners(listOfWinners)


for player in listOfPlayers:
    match = player.getAssignedMatch()
    matchNr = match.getNumber()
    matchLength = match.getLength()

    print("Player name: ", player.getName(), "Player Nr: ", player.getNumber())
    print("Match Nr: ", matchNr, "Match length: ", matchLength)
    print("")