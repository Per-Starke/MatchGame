__author__ = 'Per'

from Match_class import Match

class Player(object):

    def __init__(self, name, number, assignedMatch):
        self.Name = name
        self.Number = number
        self.AssignedMatch = assignedMatch
        self.Victory = None

    def getName(self):
        return self.Name

    def getNumber(self):
        return self.Number

    def getAssignedMatch(self):
        return self.AssignedMatch

    def getVictory(self):
        return self.Victory

    def getLengthFromAssignedMatch(self):
        lengthFromAssignedMatch = self.AssignedMatch.getLength()

    def assignVictory(self):
        //

