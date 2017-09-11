import re
f = open('text.txt', 'r')
text = f.read()
textFiltr = text.replace(' ','')
#textSplit = textFiltr.split('AB')
inp = 'AB'
res = [textFiltr[i+2] for i in range(len(textFiltr) - 2) if inp == (textFiltr[i] + textFiltr[i+1])]
print(res)
acc=[]
#for i in range(len(textFiltr)):
#    if vvod == textFiltr[i]:
#        acc.append()
#result = re.findall(r'^AB',textFiltr)
#print(result)
#print(textFiltr)
#print(textSplit)
#arr=[]
#acc=[]
#for i in range(len(textFiltr)):
#    arr.append(textFiltr[i])
#print(arr)
#vvod = ['A','B']
#kolvo=arr.count('A')
#print(kolvo)
##acc=[]
#for i in range(len(arr)):
#    if vvod == arr[i]:
#        acc.append(i)
#print(acc)