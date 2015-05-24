NPM Coding Assignment
=====================
Author: Rohit Aswani

Description
===========
This program generates a summarized report on url hit count, sorted from highest hit count to lowest count, organized daily with the earliest date appearing first using GMT time zone. 

Command Line Syntax
===================
python summary.py <input file name>

In this program, the filename is named as input.txt. 

High Level Approach
===================
I chose Python as the language to write this program. In this program, I read the input file line by line and then convert its epoch time in GMT. I created a dictionary where I store date as key and the list of urls as value. After sorting it, I calculate url hit count of the list which returns a dictionary. This dictionary has url as key and url hit count as value which is then sorted and iterated over to generate the desired output. 

Challenges
==========
The biggest challenge was to figure out what data structure to use that would provide better time complexity. I decided to use dictionary in my program because of use of dictionary allows fast lookup. It takes same amount of time to search as it takes to add data. In my program, a logical connection between date and url hit count with url was required, and hence, I decided to choose dictionary as my data structure. The complexity of the program is calculated as follows:

Complexity: O(nm)
 where n = number of dates
       m = number of urls

Testing
=======
I mainly tested the program using print statements. 
