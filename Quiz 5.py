# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION
#
# Uses National Data on the relative frequency of given names in the
# population of U.S. births, stored in a directory "names", in files
# named "yobxxxx.txt with xxxx (the year of birth)
# ranging from 1880 to 2018.
# The "names" directory is a subdirectory if the working directory.
# Prompts the user for a male first name, and finds out the years
# when this name was most popular in terms of ranking amongst male names.
# Displays the ranking, and the years in decreasing order of frequency,
# computed, for a given year, as the count of the name for the year
# divided by the sum of the counts of all male names for the year.


import csv
from pathlib import Path

cwd = Path.cwd()
possible_path_1 = cwd.parent.parent / 'names'
possible_path_2 = Path(cwd.root) / 'course' / 'data' / 'names'
if possible_path_1.exists():
    # FOR ME
    path = possible_path_1
elif possible_path_2.exists():
    # FOR ED
    path = possible_path_2
else:
    # FOR YOU, names IS A SUBDIRECTORY OF THE WORKING DIRECTORY
    path = Path('names')

# INSERT YOUR CODE HERE
name = input('Enter a male first name: ')
years_freq = {}
is_male = False
for year in range(1880,2019):
    year_path = 'yob'+str(year)+'.txt'
    text_path = Path(path) / year_path
    with open(text_path) as f:
        data = list(map(lambda x:x.replace('\n','').split(','),f.readlines()))
        f.close()
    count = 0
    all_count = 0
    for names in data:
        all_count += int(names[2])
        if names[0].lower() == name.lower():
            if names[1] == 'M':
                if names[0] == 'Franc':
                    print(names)
                is_male = True
                count+=int(names[2])
    if count>0:
        years_freq[str(year)] = count/all_count
if not(is_male):
    print(name+' is not a male first name in my records.')
    exit()
print('By decreasing order of frequency, '+name+' was most popular in the following years:')
from collections import OrderedDict
from math import ceil
years_descending = list(map(int,list(OrderedDict(sorted(years_freq.items(), reverse=True)).keys())))
for i in range(ceil(len(years_descending)/5)):
    print('    ',end='')
    print(*years_descending[5*i:5*(i+1)])
print('Its rank was '+str(max(years_freq.values()))+' then.')
