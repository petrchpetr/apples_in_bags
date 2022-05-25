"""

   A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag. Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

o   For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.


"""
from itertools import groupby
from pprint import pprint,pformat
import logging

log = logging.getLogger('apples')
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

APL=0
LEN=1
# this is the input sequence (apple types)
seq = [2,1,2,3,3,1,3,5,2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 3, 3, 1, 3, 5, 3, 4, 4, 2, 5, 3, 5, 2, 3, 4, 5, 5,4,5,5,4,4,4,4,5,5,5,4,4]
#seq = [2, 1, 2, 3, 3, 1, 3, 5]

# split it to sequences of the same numbers
# [[2, 2], [1], [2], [1], [2], [1, 1], [2, 2], [3, 3], [1], [3], [5], [3], [4, 4], [2], [5], [3], [5], [2], [3], [4], [5, 5]]
runs = [list(g) for k, g in groupby(seq)]

# calculate lengths of the sub lists {'a': apple id, 'l': length
# [{'a': 2, 'l': 2}, {'a': 1, 'l': 1}, {'a': 2, 'l': 1}, {'a': 1, 'l': 1}, {'a': 2, 'l': 1}, {'a': 1, 'l': 2}, {'a': 2, 'l': 2}, {'a': 3, 'l': 2}, {'a': 1, 'l': 1}, {'a': 3, 'l': 1}, {'a': 5, 'l': 1}, {'a': 3, 'l': 1}, {'a': 4, 'l': 2}, {'a': 2, 'l': 1}, {'a': 5, 'l': 1}, {'a': 3, 'l': 1}, {'a': 5, 'l': 1}, {'a': 2, 'l': 1}, {'a': 3, 'l': 1}, {'a': 4, 'l': 1}, {'a': 5, 'l': 2}]
sums = [(j[0],len(j),) for j in runs]

# we would be able to do this in one go with less memory as follows, but it will be even less readable
# sums = [{'a':k,'l':sum(1 for _ in g)} for k, g in groupby(seq)]

log.debug('seq %s',seq)
log.debug('runs %s',runs)
log.debug('sums %s',sums)


def is_larger3(largest,last_a,cur):
    ts = last_a[LEN]+cur[LEN]
    if ts > largest:
        largest = ts
        print("largest ",largest)
    return largest


def apples_stack3():
    global sums
    stack = []
    largest = -1
    sums = iter(sums)

    b = next(sums) # on stack
    last_a = next(sums) # the last appl and length

    cur = next(sums) # next one is current
    
    for n in sums:  
        #print("stck:",stack," cur:",cur," n:",n)
        print("last_a",last_a,"cur",cur,"n",n)
        if n[APL] == cur[APL] or n[APL] == last_a[APL] : # we continue the run
            last_a = (cur[APL],last_a[LEN] + cur[LEN],)
            cur = n           # new is the next current
        else: 
            # the new run starts with 'cur'
            largest = is_larger3(largest,last_a,cur)
            last_a = cur
            cur = n # and this is the second one

    # now check the last run
    largest = is_larger3(largest,last_a,cur)
    return largest


if __name__ == '__main__':
    largest = apples_stack3()
    print(largest)

