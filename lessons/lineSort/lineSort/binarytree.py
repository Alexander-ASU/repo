class Node:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
    def getKey(self):
        return self.key
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right
    def __str__(self):
        res = str(self.key)
        return res
class BinaryTree:
    def __init__(self):
        self._root = None
    #возвращает картеж из 2 элементов (узел, родитель)
    def _find(self, key):
        if self._root == None: return None, None
        current = self._root
        parent = None
        while key != current.key:
            if key < current.key:
                if current.getLeft() == None:
                    return None, current
                parent = current
                #cпуск
                current = current.getLeft()               
            else:
                if current.getRight() == None:
                    return None, current
                parent = current
                #cпуск
                current = current.getRight()
        return current, parent
    def add(self, node):
        ex_node, parent = self._find(node.getKey())
        if ex_node == None: 
            if parent == None:
                self._root = node
            elif parent.getKey() > node.getKey():
                 parent.setLeft(node) 
            else:
                parent.setRight(node)
        else:
            node.setLeft(ex_node.getLeft())
            node.setRight(ex_node.getRight())
            if parent.getLeft() == ex_node:
                parent.setLeft(node)
            else:
                parent.setRight(node)
    def find(self, key):
        return self._find(key)[0]
    def remove(self, key):
        node, parent = self._find(key)
        if node == None: return None
        #leaf case
        if node.getRight() == None and \
           node.getLeft() == None:
            if parent != None:
                if parent.getLeft() == node:
                    parent.setLeft(None)
                else:
                    parent.setRight(None)
            else:
                self._root = None
        #single child case
        elif node.getRight() == None or \
           node.getLeft() == None:
            node_hasLeft = node.getLeft() != None
            if parent != None:
                if parent.getLeft() == node:
                    if node_hasLeft:
                        parent.setLeft(node.getLeft())                    
                    else:
                        parent.setLeft(node.getRight())
                else:
                    if node_hasLeft:
                        parent.setRight(node.getLeft())                
                    else:
                        parent.setRight(node.getRight())
            else:
                if node_hasLeft:
                    self._root = node.getLeft()
                else:
                    self._root = node.getRight()
        else:
            curr_parent = node
            current = node.getRight()
            while current.getLeft() != None:
                #cпуск
                curr_parent = current
                current = current.getLeft()  
            if parent != None:
                if parent.getLeft() == node: 
                    parent.setLeft(current)
                else:
                    parent.setRight(current)
            else:
                self._root = current
            current.setLeft(node.getLeft())
            if curr_parent != node:
                curr_parent.setLeft(current.getRight())
                current.setRight(node.getRight())             
        node.setLeft(None)
        node.setRight(None)
        return node   

if __name__ == '__main__':
    tree1 = BinaryTree()
    node1 = Node(0)
    tree1.add(node1)
    tree1.add(Node(3))
    tree1.add(Node(2))
    tree1.add(Node(7))
    tree1.add(Node(9))
    print(tree1.find(0))
    print(tree1.find(2))
    print(tree1.find(7))
    print(tree1.find(3))
    print(tree1.find(8))