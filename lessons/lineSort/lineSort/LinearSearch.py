import re
import time
class LinearSearch:
   def __init__(self, fileName):
        self.fileName = fileName
        self.words = []
        with open(fileName) as f:
            for l in  f:
             linewords = re.split(r'\W+|\d+|_+', l)
             linewords = list(filter(bool, linewords))
             self.words.extend(linewords)
        self.words = [word.lower() for word in self.words] 
   def search(self, first, second):
        first, second = first.lower(), second.lower()
        trig = []
        for i in range(len(self.words)-2):
            if self.words[i] == first and self.words[i+1] == second:
                trig.append(self.words[i+2])
        return trig
if __name__ == '__main__':
    ls = LinearSearch('big.txt')
    while(True):
        inp = input('Enter please two first words of trigramm.\nEnter -1 to stop\n')
        if inp == '-1': break
        first, second = inp.split()
        #print(search(first, second, 'text.txt'))
        print(ls.search(first, second))
  
  
