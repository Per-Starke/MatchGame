__author__ = 'Per'

from Match_class import Match


class Player(object):

    def __init__(self, name, number, assignedMatch):
        self.Name = name
        self.Number = number
        self.AssignedMatch = assignedMatch   # Object of Match.class will be assigned here

    def getName(self):
        return self.Name

    def getNumber(self):
        return self.Number

    def getAssignedMatch(self):
        return self.AssignedMatch

