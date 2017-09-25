import re
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
    def __str__(self):
        return str(self.key) + ' ' + str(self.collDict)   
    @staticmethod 
    def makeKey(firstWord, secondWord):
        concatination = firstWord + secondWord
        return hash(concatination)
   
class BinaryTreeSearch:
    def __init__(self, fileName):
         self.tree = BinaryTree()
         with open(fileName) as f:
            for line in f:
                words = re.split(r'\W+|\d+|_+', line)                               
                for i in range(len(words) - 2):
                    w1,w2 = words[i].lower(),words[i].lower()
                    node = self.tree.find(NodeWithData.makeKey(w1, w2))
                    if node == None:
                        node = NodeWithData(w1, w2)
                        self.tree.add(node)
                    node.UpdateDict(w1, w2, words[i+2].lower())
    def search(self, first, second):
         first, second = first.lower(), second.lower()
         trig = []
         self.tree.find()
         

if __name__ == '__main__':
    #test = BinaryTreeSearch('text.txt')
     
    test1 = BinaryTreeSearch('text.txt')
    #test = NodeWithData('ONE','TWO')
    print(test1)
