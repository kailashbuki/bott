# Program Name: levenshtein.py
# Description: This module calculates the levenshtein distance between two strings
# Author: Kailash Budhathoki [kailash.buki@gmail.com][IOE, Pulchowk Campus, Nepal]
# Revision: Edited the min function to use the built-in min() function of list

def lev_dist(colStr, rowStr):
    clen = colStr.__len__()
    rlen = rowStr.__len__()
    # Instantiate a table of levenshtein distance
    table = []
    for i in xrange(rlen+1):
        table.append([])
    for i in xrange(clen+1):
        table[0].append(i)
    for j in xrange(rlen+1):
        if j==0:
            continue
        table[j].append(j)

    # Fill up the table with levenshtein distances
    for i in xrange(rlen+1):
        if i==0:
            continue
        for j in xrange(clen+1):
            if j==0:
                continue
            if rowStr[i-1] == colStr[j-1]:
                min_dist = table[i-1][j-1]
            else:
                min_dist = min(table[i-1][j]+1,table[i][j-1]+1,table[i-1][j-1]+1)
            table[i].append(min_dist)

    return table[i][j]
