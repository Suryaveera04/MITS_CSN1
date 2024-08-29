class JaccardCoefficient:
    def __init__(self, string1, string2):
        # Initialize the class with two input strings
        self.string1 = set(string1)
        self.string2 = set(string2)

    def findJaccardCoefficient(self):
        # Find the intersection of the sets (common elements between the strings)
        intersection = self.string1.intersection(self.string2)
        # Find the union of the sets (all unique elements from both strings)
        union = self.string1.union(self.string2)

        # Calculate the lengths of the intersection and union sets
        intersectionLength = len(intersection)
        unionLength = len(union)

        # Calculate the Jaccard index: intersection length / union length
        jaccardIndex = intersectionLength / unionLength

        # Compute the Jaccard coefficient: 1 - Jaccard index
        jaccardCoeff = 1 - jaccardIndex

        return jaccardCoeff

# Create an instance of the JaccardCoefficient class with input strings "surya" and "sunil"
obj = JaccardCoefficient("surya", "sunil")
# Print the calculated Jaccard coefficient
print(obj.findJaccardCoefficient())
