from __future__ import division
from levenshtein import *
string1 = raw_input()
string2 = raw_input()

list1 = string1.split(' ')
list2 = string2.split(' ')

len_list1 = list1.__len__()
len_list2 = list2.__len__()

count = 0 
for i in list1:
	for j in list2: 	
		d = lev_dist(i, j)
		if d<2:
			count +=1
			break
print '='*75
if count/len_list1 >=0.5:
	print string2,'is in the knowledgebase'
else:
	print 'sorry! chap'
print '='*75		
