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

def assignLengthToMatches(listOfMatches):
    for match in listOfMatches:
        match.Length = False
    listOfMatches[0].Length = True
    return listOfMatches

def shuffleListOfMatchesAndAssignToPlayers(listOfMatches, listOfPlayers):
    random.shuffle(listOfMatches)
    i = 0
    for match in listOfMatches:
        listOfPlayers[i].AssignedMatch = match
        i += 1

def assignVictory(listOfPlayers):
    for player in listOfPlayers:
        if player.AssignedMatch.getLength() == True:
            player.Victory = True
            winner = player
        else:
            player.Victory = False
    return winner

listOfPlayers = defineListOfPlayers()

listOfMatches = defineListOfMatches(listOfPlayers)

listOfMatches = assignLengthToMatches(listOfMatches)

shuffleListOfMatchesAndAssignToPlayers(listOfMatches, listOfPlayers)

winner = assignVictory(listOfPlayers)

print("")
print("The winner is " + winner.getName())
print("")



for player in listOfPlayers:
    match = player.getAssignedMatch()
    matchNr = match.getNumber()
    matchLength = match.getLength()

    print("Player name: ", player.getName(), "Player Nr: ", player.getNumber())
    print("Match Nr: ", matchNr, "Match length: ", matchLength)
    print("")