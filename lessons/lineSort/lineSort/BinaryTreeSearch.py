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
            flag = False
            lastWord = ''
            preLastWord = ''
            oneWordLineWord = ''
            for line in f:
                words = re.split(r'\W+|\d+|_+', line)
                words = list(filter(bool, words))
                if len(words) == 0: continue
                if oneWordLineWord != '':
                    words.insert(0, oneWordLineWord)
                    oneWordLineWord = ''
                if len(words) == 1:
                    oneWordLineWord = words[0].lower()
                    continue
                if flag:
                    #pre last first
                    node = self.tree.find(NodeWithData.makeKey(preLastWord, lastWord))
                    if node == None:
                        node = NodeWithData(preLastWord, lastWord)
                        self.tree.add(node)
                    node.UpdateDict(preLastWord, lastWord, words[0].lower())
                    #last first second
                    node = self.tree.find(NodeWithData.makeKey(lastWord, words[0].lower()))
                    if node == None:
                        node = NodeWithData(lastWord, words[0].lower())
                        self.tree.add(node)
                    node.UpdateDict(lastWord, words[0].lower(), words[1].lower())
                else: flag = True                             
                lastWord = words[-1].lower()                      
                preLastWord = words[-2].lower()
                for i in range(len(words) - 2):
                    w1 = words[i].lower()
                    w2 = words[i + 1].lower()
                    node = self.tree.find(NodeWithData.makeKey(w1, w2))
                    if node == None:
                        node = NodeWithData(w1, w2)
                        self.tree.add(node)
                    node.UpdateDict(w1, w2, words[i+2].lower())
            if oneWordLineWord + preLastWord + lastWord != '':
                node = self.tree.find(NodeWithData.makeKey(preLastWord, lastWord))
                if node == None:
                    node = NodeWithData(preLastWord, lastWord)
                    self.tree.add(node)
                node.UpdateDict(preLastWord, lastWord, oneWordLineWord)
    
    def search(self, first, second):
        first, second = first.lower(), second.lower()
        key = NodeWithData.makeKey(first, second)
        node = self.tree.find(key)
        if node == None: return []
        return node.GetTrigrams(first, second)  

if __name__ == '__main__':
    def test_searh_in_tree(tree, w1, w2):
        print(w1, w2, '=', tree.search(w1, w2))
    tree1 = BinaryTreeSearch('text.txt')
    test_searh_in_tree(tree1, 'A', 'B')
    test_searh_in_tree(tree1, 'B', 'C')
    test_searh_in_tree(tree1, 'C', 'D')
    test_searh_in_tree(tree1, 'D', 'A')
    test_searh_in_tree(tree1, 'B', 'E')
    test_searh_in_tree(tree1, 'E', 'D')
    test_searh_in_tree(tree1, 'Z', 'F')
    test_searh_in_tree(tree1, 'B', 'F')
    test_searh_in_tree(tree1, 'F', 'A')
    test_searh_in_tree(tree1, 'B', 'Z')
    test_searh_in_tree(tree1, 'Z', 'E')
    test_searh_in_tree(tree1, 'E', 'O')
    pass
