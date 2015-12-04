__author__ = 'Per'

from Match_class import Match
from Player_class import Player
import random


numberOfPlayers = input("how many players? ")


def defineListOfPlayers():   # returs a list of Objects of Player_class, name = input

    listOfPlayers = []

    for i in range (0, numberOfPlayers):
        playerName = raw_input("Player name: ")
        matchToAssingToPlayer = Match(i)
        player_i = Player(playerName, i, matchToAssingToPlayer)
        listOfPlayers.append(player_i)

    return listOfPlayers

def defineListOfMatches(listOfPlayers):  # returs a list of Objects of Match_class, assigns Match x to Player x

    listOfMatches = []

    for player in listOfPlayers:
        match = player.getAssignedMatch()
        listOfMatches.append(match)

    return listOfMatches

def assignLengthToMatches(listOfMatches, nrOfLongMatches):  # for a given number of winners, in range 0 to x, length = True will be assigned to list of Matches
    for match in listOfMatches:  # first, all Length = False
        match.Length = False
    for i in range (0, nrOfLongMatches):  # for given number, Length = True
        listOfMatches[i].Length = True
    return listOfMatches


def shuffleListOfMatchesAndAssignToPlayers(listOfMatches, listOfPlayers):  # randomly shuffles 
    random.shuffle(listOfMatches)
    i = 0
    for match in listOfMatches:
        listOfPlayers[i].AssignedMatch = match
        i += 1

def assignVictory(listOfPlayers):
    listOfWinners = []
    for player in listOfPlayers:
        if player.AssignedMatch.getLength() == True:
            listOfWinners.append(player)
    return listOfWinners

def printWinners(listOfWinners):
    for winner in listOfWinners:
        print("One Winner is '" + winner.getName() + "' with the player-number " + str(winner.getNumber()))

def printLoosers(listOfPlayers):
    for player in listOfPlayers:
        if player.AssignedMatch.getLength() != True:
            print("One Looser is '" + player.getName() + "' with the player-number " + str(player.getNumber()))


listOfPlayers = defineListOfPlayers()

listOfMatches = defineListOfMatches(listOfPlayers)

nrOfWinners = input("Nr of winners: ")

print("")

listOfMatches = assignLengthToMatches(listOfMatches, nrOfWinners)

shuffleListOfMatchesAndAssignToPlayers(listOfMatches, listOfPlayers)

listOfWinners = assignVictory(listOfPlayers)

printWinners(listOfWinners)
print("")
printLoosers(listOfPlayers)

# for player in listOfPlayers:
#     match = player.getAssignedMatch()
#     matchNr = match.getNumber()
#     matchLength = match.getLength()
#
#     print("Player name: ", player.getName(), "Player Nr: ", player.getNumber())
#     print("Match Nr: ", matchNr, "Match length: ", matchLength)
#     print("")