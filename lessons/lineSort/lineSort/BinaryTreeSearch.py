from binarytree import Node, BinaryTree
#import hashlib
class NodeWithData(Node):
    def __init__(self, firstWord, secondWord):
        key = NodeWithData.makeKey(firstWord, secondWord)
        super().__init__(key)
        self.firstWord = firstWord
        self.secondWord = secondWord 
        concatination = firstWord + secondWord
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
         self.tree = BinaryTree()
         with open(fileName) as f:
            for line in f:
                flag = True
                words = re.split(r'\W+|\d+|_+', line)                               
                for i in range(len(words)):
                    if flag:
                        self.tree.add(NodeWithData(words[i], words[i+1]))
                        if i == max(len(words)):
                            flag = False
                            break
                    self.tree.add(NodeWithData(words[i], words[i+1]))
if __name__ == '__main__':
    test = NodeWithData('ONE','TWO')
    print(test)