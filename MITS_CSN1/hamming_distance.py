class HammingDistance:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def findHammingDistance(self):
        str1 = self.string1
        str2 = self.string2

        if len(str1) != len(str2) : return "Both the Strings should be equal"

        distance = 0

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                distance+=1

        return distance