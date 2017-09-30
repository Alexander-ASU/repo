import re
from binarytree import Node, BinaryTree
#import hashlib
class NodeWithData(Node):
    def __init__(self, firstWord, secondWord):
        key = NodeWithData.makeKey(firstWord, secondWord)
        super().__init__(key) 
        concatination = firstWord + secondWord
        self.collDict = {concatination: {}}
    def UpdateDict(self, firstWord, secondWord, thirdWord):
        concatination = firstWord + secondWord
        trigs = self.collDict.get(concatination, {})
        count = trigs.get(thirdWord, 0)
        trigs[thirdWord] = count + 1
        self.collDict[concatination] = trigs   
    def GetTrigrams(self, firstWord, secondWord):
        concatination = firstWord + secondWord
        if concatination in self.collDict:
            return list(self.collDict[concatination].keys())            
        return [] 
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
            flag = 0 
            for line in f:
                words = re.split(r'\W+|\d+|_+', line)
                words = list(filter(bool, words))
                #if flag != 0:                              
                for i in range(len(words) - 2):
                    if flag == 0 and i == len(words) - 3:
                        ferstWordOneLine = words[i + 1].lower()
                        secondWordOneLine = words[i + 2].lower()
                        node = self.tree.find(NodeWithData.makeKey(ferstWordOneLine, secondWordOneLine))
                       # node.UpdateDict(ferstWordOneLine, secondWordOneLine, words[i+2].lower())
                        flag = flag + 1 
                        break
                    if i == len(words) - 3:
                        oneWord = words[i + 1].lower()
                        twoWord = words[i + 2].lower()
                        node = self.tree.find(NodeWithData.makeKey(oneWord, twoWord))
                    else:
                        w1,w2 = words[i].lower(),words[i + 1].lower()
                        node = self.tree.find(NodeWithData.makeKey(w1, w2))
                        if node == None:
                            node = NodeWithData(w1, w2)
                            self.tree.add(node)
                        node.UpdateDict(w1, w2, words[i+2].lower())
    
    def search(self, first, second):
        first, second = first.lower(), second.lower()
        key = NodeWithData.makeKey(first, second)
        node = self.tree.find(key)
        if node == None: return []
        return node.GetTrigrams(first, second)  

if __name__ == '__main__':
    #test = BinaryTreeSearch('text.txt')
     
    test1 = BinaryTreeSearch('text.txt')
    test2 = test1.search('A', 'B')
    #test = NodeWithData('ONE','TWO')
    print(test2)
