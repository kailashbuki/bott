from __future__ import division
from levenshtein import *

colStr = 'reminiscent'
rowStr = 'reminiscence'
clen = colStr.__len__()
rlen = rowStr.__len__()
if clen<rlen:
    maxDist = rlen
else:
    maxDist = clen
distance = lev_dist(colStr, rowStr)
decCost = distance/maxDist
if decCost<0.3:
    print 'Bingo! These are almost the same'
else:
    print 'Nope! Not close enough'

