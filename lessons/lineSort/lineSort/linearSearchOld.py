import re
def searchOld(first, second, fileName):
    words = []
    with open(fileName) as f:
        for l in  f:
            linewords = re.split(r'\W+|\d+|_+', l)
            linewords = list(filter(bool, linewords))
            words.extend(linewords)
        words = [word.lower() for word in words] 
    first, second = first.lower(), second.lower()
    trig = []
    for i in range(len(words)-2):
        if words[i] == first and words[i+1] == second:
            trig.append(words[i+2])
    return trig
