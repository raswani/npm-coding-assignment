#!/usr/bin/python
import sys
import time
from collections import OrderedDict, Counter
import collections

with open(sys.argv[1]) as f:
    lines = f.readlines()

date_dict = dict()
list = []
for line in lines:
    line = line.strip()
    time_epoch = line.split('|')[0]  # Splitting each line and extracting epoch time
    time_gmt = time.strftime('%m/%d/%Y', time.localtime(float(time_epoch)))  # Converting epoch time into GMT standard
    url = line.split('|')[1]
    list.append((url, time_gmt))


sorted_list = sorted(list, key=lambda x:x[1])

counter=collections.Counter(sorted_list)

sorted_dict = sorted(counter.items(), key=lambda t:t[1])


for item in sorted_dict:
    date = item[0][1]
    item_url = item[0][0]
    count = item[1]
    tuple = (item_url, count)
    if date in date_dict:
        item_list = date_dict[date]
        item_list.append(tuple)
        date_dict[date] = item_list
    else:
        date_dict[date] = [tuple]


#print date_dict

sorted_date_dict = OrderedDict(sorted(date_dict.items(), key=lambda t:t[0]))

#print sorted_date_dict

for item in sorted_date_dict:
    print item + " GMT"
    sorted_val = sorted(sorted_date_dict[item], key=lambda t : -t[1])
    print '\n'.join(map(str, sorted_val))\
        .replace('(\'', '')\
        .replace('\',', " ")\
        .replace(')', '')
