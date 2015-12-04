__author__ = 'Per'

class Match (object):

    def __init__(self, number):
        self.Number = number
        self.Length = None   # will be assigned in assignLengthToMatches function

    def getNumber(self):
        return self.Number

    def getLength(self):
        return self.Length

