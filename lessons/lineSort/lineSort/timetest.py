import time
from linearSearchOld import searchOld
from LinearSearch import LinearSearch

def mesuareCall(func, *args, **kwargs):
    acc = 0
    count = kwargs.get('count', 1)
    for i in range(count):
        start = time.time()
        func(*args)
        acc += time.time() - start
    return acc / count

if __name__ == '__main__':
    #print('linearSearchOld ' + str(mesuareCall(searchOld, \
    #    'The', 'Project', 'big.txt', count=3)) + ' s')
    ls = LinearSearch('big.txt')
    print('linearSearch ' + str(mesuareCall(ls.search, \
        'The', 'Project')) + ' s')