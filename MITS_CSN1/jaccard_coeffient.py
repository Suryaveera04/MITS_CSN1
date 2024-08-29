class JaccardCoefficient:
    def __init__(self, string1, string2):
        self.string1 = set(string1)
        self.string2 = set(string2)

    def findJaccardCoefficient(self):
        intersection = self.string1.intersection(self.string2)
        union = self.string1.union(self.string2)

        intersectionLength = len(intersection)

        unionLength = len(union)

        jaccardIndex = intersectionLength/unionLength

        jaccardCoeff = 1- jaccardIndex

        return jaccardCoeff
obj=JaccardCoefficient("surya","sunil")
print(obj.findJaccardCoefficient())