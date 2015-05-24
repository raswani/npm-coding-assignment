#!/usr/bin/python
import sys
import os
import time
from collections import OrderedDict, Counter

with open(sys.argv[1]) as f:
	lines = f.readlines()

date_dict = dict()
for line in lines:
	line = line.strip()
	time_epoch = line.split('|')[0]				#Splitting each line and extracting epoch time
	time_gmt = time.strftime('%m/%d/%Y' , time.localtime(float(time_epoch)))   #Converting epoch time into GMT standard
	url = line.split('|')[1]
	if time_gmt in date_dict:
		date_dict[time_gmt].append(url)
	else:
		date_dict[time_gmt] = [url]

'''
Sorting the dictionary (Key: date, value: list of urls)
'''
sorted_dict = OrderedDict(sorted(date_dict.items(), key=lambda t: t[0]))

for key, value in sorted_dict.items():
	print key + ' GMT' 	
	dict_count = Counter(value)
	#print list_elements
	ordered_count = OrderedDict(sorted(dict_count.items(), key=lambda t: t[1], reverse = True)) #Soring the dictionary 
	for each_url in ordered_count:
		print each_url +' '+ str(ordered_count[each_url])