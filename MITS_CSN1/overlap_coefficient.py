class overlapCoefficient:

    def __init__(self, string1, string2):
        self.string1 = set(string1)
        self.string2 = set(string2)

    def findOverlapCoefficient(self):

        intersection = self.string1.intersection(self.string2)

        string1length = len(self.string1)

        string2length = len(self.string2)

        intersectionLength = len(intersection)

        overlapIndex = intersectionLength / min(string1length,string2length)

        overlapCoeff = 1 - overlapIndex

        return overlapCoeff;