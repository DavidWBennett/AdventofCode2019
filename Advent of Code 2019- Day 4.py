# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:14:34 2019

@author: dbge
"""

"""
However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?
"""

#Part 1
pw_range = range(136760,595730) #458,940 is the length

passwords = []
for i in pw_range:
    passwords.append(str(i))
passwords
#Must contain a set of adjacent, repeating digits
passwords = [x for x in passwords if "00" in x or "99" in x or "88" in x or "77" in x or "66" in x or "55" in x or "44" in x or "33" in x or "22" in x or "11" in x]

#Use this code to see if passwords contain non-descending digits (True, False)
passwords_boolean = []
for i in range(len(passwords)):
    passwords_boolean.append(int(passwords[i][5]) >= int(passwords[i][4]) >= int(passwords[i][3]) >= int(passwords[i][2]) >= int(passwords[i][1]) >= int(passwords[i][0]))

from itertools import compress #https://stackoverflow.com/questions/18665873/filtering-a-list-based-on-a-list-of-booleans
passwords = list(compress(passwords, passwords_boolean))
len(passwords) #1873

#Part 2
"""
An Elf just remembered one more important detail: the two adjacent matching digits are not part of a larger group of matching digits.
In other words, we can't have a threesome/foursome of repeated numbers UNLESS there is a second set of only 2 repeated numbers.
"""
# six digits in a row are no longer acceptable
passwords = [x for x in passwords if "000000" not in x and "999999" not in x and "888888" not in x and "777777" not in x and "666666" not in x and "555555" not in x and "444444" not in x and "333333" not in x and "222222" not in x and "111111" not in x]
# five digits in a row are no longer acceptable
passwords = [x for x in passwords if "00000" not in x and "99999" not in x and "88888" not in x and "77777" not in x and "66666" not in x and "55555" not in x and "44444" not in x and "33333" not in x and "22222" not in x and "11111" not in x]
len(passwords) #1820

# Addres 4 digit passwords
num4_digits = ["0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999"]
num3_digits = ["000", "111", "222", "333", "444", "555", "666", "777", "888", "999"]
num2_digits = ["00", "11", "22", "33", "44", "55", "66", "77", "88", "99"]

passwords4 = [x for x in passwords if "0000" in x or "9999" in x or "8888" in x or "7777" in x or "6666" in x or "5555" in x or "4444" in x or "3333" in x or "2222" in x or "1111" in x]
len(passwords4) #233

import re
sample = []
for i in range(len(passwords4)):
    for k in num4_digits:
        if k in passwords4[i]:
            sample.append(re.split(k, passwords4[i]))

sample_boolean = []
for i in range(len(sample)):
    if "00" in sample[i][0] or "11" in sample[i][0] or "22" in sample[i][0] or "33" in sample[i][0] or "44" in sample[i][0] or "55" in sample[i][0] or "66" in sample[i][0] or "77" in sample[i][0] or "88" in sample[i][0] or "99" in sample[i][0]:
        sample_boolean.append(False)
    else:
        sample_boolean.append(True)
for i in range(len(sample)):
    if "00" in sample[i][1] or "11"  in sample[i][1] or "22"  in sample[i][1] or "33" in sample[i][1] or "44" in sample[i][1] or "55" in sample[i][1] or "66" in sample[i][1] or "77"  in sample[i][1] or "88" in sample[i][1] or "99" in sample[i][1]:
        sample_boolean[i] = False
passwords4 = list(compress(passwords4, sample_boolean))      
len(passwords4) #189
passwords = set(passwords).difference(set(passwords4))
passwords = list(passwords)
len(passwords) #1631

# Passwords with 3 repeating digits and no 2 repeating digits.
passwords3 = [x for x in passwords if "000" in x or "999" in x or "888" in x or "777" in x or "666" in x or "555" in x or "444" in x or "333" in x or "222" in x or "111" in x]
len(passwords3) #753
#Eliminate the password3 values that have two sets of 3.
passwords3_boolean = []
for i in range(len(passwords3)):
    if passwords3[i][0] == passwords3[i][1] == passwords3[i][2] and passwords3[i][3] == passwords3[i][4] == passwords3[i][5]:
        passwords3_boolean.append(False)
    else:
        passwords3_boolean.append(True)
passwords3 = list(compress(passwords3, passwords3_boolean))      
len(passwords3) #731

sample = []
for i in range(len(passwords3)):
    for k in num3_digits:
        if k in passwords3[i]:
            sample.append(re.split(k, passwords3[i]))
len(sample) #731

sample_boolean = []
for i in range(len(sample)):
    if "00" in sample[i][0] or "11" in sample[i][0] or "22" in sample[i][0] or "33" in sample[i][0] or "44" in sample[i][0] or "55" in sample[i][0] or "66" in sample[i][0] or "77" in sample[i][0] or "88" in sample[i][0] or "99" in sample[i][0]:
        sample_boolean.append(False)
    else:
        sample_boolean.append(True)
for i in range(len(sample)):
    if "00" in sample[i][1] or "11" in sample[i][1] or "22" in sample[i][1] or "33" in sample[i][1] or "44" in sample[i][1] or "55" in sample[i][1] or "66" in sample[i][1] or "77" in sample[i][1] or "88" in sample[i][1] or "99" in sample[i][1]:
        sample_boolean[i] = False
len(sample_boolean) #731
passwords3 = list(compress(passwords3, sample_boolean))  #I think there might be a problem here.    
#This list is pretty good, but the problem is if there is a run of 3 and another run of 3.
passwords = set(passwords).difference(set(passwords3))
passwords = list(passwords)
len(passwords) #1286

#Eliminate the password3 values that have two sets of 3.
passwords_boolean = []
for i in range(len(passwords)):
    if passwords[i][0] == passwords[i][1] == passwords[i][2] and passwords[i][3] == passwords[i][4] == passwords[i][5]:
        passwords_boolean.append(False)
    else:
        passwords_boolean.append(True)
passwords = list(compress(passwords, passwords_boolean))      
len(passwords) #1264