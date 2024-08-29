class OverlapCoefficient:
    def __init__(self, string1, string2):
        """
        Initializes an instance of the OverlapCoefficient class.

        Args:
            string1 (str): First input string.
            string2 (str): Second input string.
        """
        self.string1 = set(string1)
        self.string2 = set(string2)

    def findOverlapCoefficient(self):
        """
        Calculates the overlap coefficient between the two input strings.

        Returns:
            float: The overlap coefficient (a value between 0 and 1).
        """
        intersection = self.string1.intersection(self.string2)
        string1length = len(self.string1)
        string2length = len(self.string2)
        intersectionLength = len(intersection)
        overlapIndex = intersectionLength / min(string1length, string2length)
        overlapCoeff = 1 - overlapIndex
        return overlapCoeff
