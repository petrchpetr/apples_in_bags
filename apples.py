"""

   A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag. Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

o   For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.


"""
from itertools import groupby
from pprint import pprint,pformat
import logging

log = logging.getLogger('apples')
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# this is the input sequence (apple types)
seq = [2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 3, 3, 1, 3, 5, 3, 4, 4, 2, 5, 3, 5, 2, 3, 4, 5, 5]
#seq = [2, 1, 2, 3, 3, 1, 3, 5]

# split it to sequences of the same numbers
# [[2, 2], [1], [2], [1], [2], [1, 1], [2, 2], [3, 3], [1], [3], [5], [3], [4, 4], [2], [5], [3], [5], [2], [3], [4], [5, 5]]
runs = [list(g) for k, g in groupby(seq)]

# calculate lengths of the sub lists {'a': apple id, 'l': length
# [{'a': 2, 'l': 2}, {'a': 1, 'l': 1}, {'a': 2, 'l': 1}, {'a': 1, 'l': 1}, {'a': 2, 'l': 1}, {'a': 1, 'l': 2}, {'a': 2, 'l': 2}, {'a': 3, 'l': 2}, {'a': 1, 'l': 1}, {'a': 3, 'l': 1}, {'a': 5, 'l': 1}, {'a': 3, 'l': 1}, {'a': 4, 'l': 2}, {'a': 2, 'l': 1}, {'a': 5, 'l': 1}, {'a': 3, 'l': 1}, {'a': 5, 'l': 1}, {'a': 2, 'l': 1}, {'a': 3, 'l': 1}, {'a': 4, 'l': 1}, {'a': 5, 'l': 2}]
sums = [{'a':j[0],'l':len(j)} for j in runs]

# we would be able to do this in one go with less memory as follows, but it will be even less readable
# sums = [{'a':k,'l':sum(1 for _ in g)} for k, g in groupby(seq)]


log.debug('seq %s',seq)
log.debug('runs %s',runs)
log.debug('sums %s',sums)


#find all the sequences
finals=[] # put the final sequences here

# now we will look for the longest run of two types of apples
# start with the second apple type so I can always go at least one step back as we search backwards 

for k in range(1,len(sums),1):
    log.info("k:%d",k)

    # keys are the two apple ids I do consider
    keys=set([sums[k]['a'],sums[k-1]['a']])

    # from the index k I search left for the longest sequence (run)
    kk = k
    run =[]
    while(kk>=0):
        ai=sums[kk]['a'] # current apple id
        if ai in keys: # if it is in the considered keys, continue and add it to the run
            run.append(sums[kk])
        else: # it is a 3rd apple id, stop
            break
        kk -= 1

    # calculate a length of the run
    ssum=sum([i['l'] for i in run])
    log.debug("RUN(apples(%s):length(%d),detail(%s)",keys,ssum,run)
    finals.append(
            {
                'keys': keys,
                'length': ssum,
                'run': run
            })



log.debug('finals')
log.debug(pformat(finals))

l=-1 # the longest run
longest={} # details of the sequence
for k in finals:
    if k['length'] > l:
        longest=k
        l=longest['length']

log.debug("longest: %s",longest)
print(longest['length'])




