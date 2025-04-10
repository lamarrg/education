"""
Open a .txt file and count the frequency of each word.
(Words only — strip punctuation before counting.)
"""

import string

# create empty dictionary to hold word counts
word_count={}

with open("words_to_count.txt", "r", encoding="utf-8") as source_text:
    # read text of file
    raw_text = source_text.read()

    # removes all punctuations, line brakes and creates a list of individual words at spaces
    clean_text = list(raw_text.translate(str.maketrans('','', string.punctuation)).replace('\n', ' ').split(' '))


# iterates over list of words
for i in clean_text:
    if i.lower() in word_count:
         # if word is in dictionary, increase count total by 1
        word_count[i.lower()]+=1
    else:
        # if word is not in dictionary, create entry and initialize count to 1
        word_count[i.lower()]=1

print(word_count)