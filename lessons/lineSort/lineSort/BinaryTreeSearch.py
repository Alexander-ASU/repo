from binarytree import Node
#import hashlib
class NodeWithData(Node):
    def __init__(self, firstWord, secondWord, fileName):
        concatination = firstWord + secondWord
        key = hash(concatination)
        super().__init__(key)
        self.firstWord = firstWord
        self.secondWord = secondWord 
        self.collDict = {concatination: {}}
    def UpdateDict(self, firstWord, secondWord, thirdWord):
        concatination = firstWord + secondWord
        trigs = self.collDict.get(concatination, {})
        count = trigs.get(thirdWord, 0)
        trigs[thirdWord] = count + 1
        self.collDict[concatination] = trigs
         
    @staticmethod 
    def makeKey(firstWord, secondWord):
        concatination = firstWord + secondWord
        return hash(concatination)
   
class BinaryTreeSearch:
    def __init__(self, fileName):
         with open(fileName) as f:
            buffer = ''
            for line in f:
                linewords = re.split(r'\W+|\d+|_+', line)
                for i in range(linewords):
                    node = twoWords[i] + twoWords[i + 1]
                    if self.firstWord[:-1]: 
                        buffer = self.firstWord
                        break
if __name__ == '__main__':
    test = NodeWithData('ONE','TWO')
    print(test)