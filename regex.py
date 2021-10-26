#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:25:44 2021

@author: carolyndavis
"""

import re 


# =============================================================================
# 1.) Write a function named is_vowel. It should accept a string as input and use a regular expression
#  to determine if the passed string is a vowel. While not explicity mentioned in the lesson, you
#  can treat the result of re.search as a boolean value that indicates whether or not the regular
#  expression matches the given string
# =============================================================================

# regex = '.[aeiouAEIOU][A-Za-z0-9_]+'
     
# Define a function for
# accepting string start with vowel
def is_vowel(string):
    '''
    This function takes in a string and returns
    whether the string contains a vowel.
    '''
    regex = '.[aeiouAEIOU][A-Za-z0-9_]+'
 
     # pass the regular expression
     # and the string in search() method
    if(re.search(regex, string)):
        return True
         
    else:
        return False


string = input('Enter a string: ')


is_vowel(string)



# =============================================================================
# 2.) Write a function named is_valid_username that accepts a string as input.
#  A valid username starts with a lowercase letter, and only consists of
#  lowercase letters, numbers, or the _ character. It should also be no longer
#  than 32 characters. The function should return either True or False depending
#  on whether the passed string is a valid username.
# =============================================================================

# regex = '^(?=[a-z0-9_]{5,32}$)(?!.*[_]{2})[^_].*[^_]$'

def is_valid_username(string):
    '''
     This function takes in an input string for username
    and assesses whether it only consists of lowercase letters,
    numbers, and underscores.  If username contains more than one 
    underscore or is past 32 character count limit, it will be returned
    as invalid.
    '''
     # pass the regular expression
     # and the string in search() method
    
    regex = '^(?=[a-z0-9_]{5,32}$)(?!.*[_]{2})[^_].*[^_]$'
    
    if(re.search(regex, string)):
        return True
         
    else:
        return False


string = input('Enter a string: ')


is_valid_username(string)



# =============================================================================
# 3.) Write a regular expression to capture phone numbers. It should match all of the following:
# (210) 867 5309
# +1 210.867.5309
# 867-5309
# 210-867-5309
# =============================================================================



def is_phone_number(string):
    '''
    This function takes in a string of numbers and return whether
    the input is a phone number.
    '''
    regex = '^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$'
    
    if(re.search(regex, string)):
        return True
         
    else:
        return False


string = input('Enter a string: ')

is_phone_number(string)




# =============================================================================
# 4.) Use regular expressions to convert the dates below to the standardized year-month-day format.
# 02/04/19
# 02/05/19
# 02/06/19
# 02/07/19
# 02/08/19
# 02/09/19
# 02/10/19
# =============================================================================


import pandas as pd

from datetime import datetime
sample_dates = pd.Series(['02/04/19', '02/05/19', '02/06/19', '02/07/19', '02/08/19', '02/09/19', '02/10/19'])
sample_dates = [str (i) for i in sample_dates]
sample_dates.describe()

sample_dates= pd.to_datetime(sample_dates[1:]).strftime('%Y-%m-%d')
print(sample_dates)




# =============================================================================
# 5.) Write a regex to extract the various parts of these logfile lines:
# =============================================================================
# =============================================================================
# GET /api/v1/sales?page=86 [16/Apr/2019:193452+0000] HTTP/1.1 {200} 510348 "python-requests/2.21.0" 97.105.19.58
# POST /users_accounts/file-upload [16/Apr/2019:193452+0000] HTTP/1.1 {201} 42 "User-Agent: Mozilla/5.0 (X11; Fedora; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" 97.105.19.58
# GET /api/v1/items?page=3 [16/Apr/2019:193453+0000] HTTP/1.1 {429} 3561 "python-requests/2.21.0" 97.105.19.58
# 
# =============================================================================






# regexp = r'(\d{4})-(\d{2})-(\d{2})'
# sample_dates = pd.Series(['02/04/19', '02/05/19', '02/06/19', '02/07/19', '02/08/19', '02/09/19', '02/10/19'])
# sample_dates.str.replace(regexp, r'\2/\3/\1')


# re.sub(r'(\d{4})(\d{2})(\d{2})', r'\2/\3/\1', datestring)
# (\d{4})-(\d{1,2})-(\d{1,2})
# def standard_date(datestring):
#     regex = '(\d{4})/(\d{1,2})/(\d{1,2})'
#     if(re.sub(regex, datestring)):
#         return True
    
#     else:
#         return False


# datestring = input('Enter a string: ')

# standard_date(datestring)

# regexp = r'(\d{1,2})-(\d{1,2})-(\d{4})'

# sample_dates.str.replace(regexp, r'\3/\2/\1')
# print(sample_dates)

# def change_date_format(dt):
#         return re.sub(r'(\d{1,2})-(\d{1,2})-(\d{4})', '\\4-\\2-\\1', dt)
# # dt1 = "2026-01-02"
# print("Original date in YYY-MM-DD Format: ",sample_dates)
# print("New date in DD-MM-YYYY Format: ",change_date_format(sample_dates))

# sample_dates = list(sample_dates)
# sample_dates = sample_dates[1:]
# test = datetime.strptime(sample_dates, "%m/%d/%Y").strftime('%Y-%m-%d')


# sample_dates = pd.Series(sample_dates)




# print(sample_dates)



# sample_dates.replace(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/, "$3/\$2\/-$1")


# sentence = "My name is carolyn."

# word = "a"



# def find_m(word):
#     vowel = re.match("[^aeiou]*[aeiou]*$",word)
#     if word == vowel:
#         return True
#     else:
#         if word != vowel:
#             return False

# find_m(word)




# word = input('Enter a string: ')
# found = re.search(r'aeiou', word)
# if found:
#     print(word, 'contains the vowel.')
# else:
#     print(word, 'does not contain the vowel.')
    
    
    
    
# word = input('Enter a word:')
# try: 
#     print(re.search('[aeiou]', word, re.I).start())
# except AttributeError:
#     print('No vowels found in word')
