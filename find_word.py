#!/usr/bin/python
# -*- coding: utf-8 -*-
 
puzzle='''E N V L P T Y O M G H
S O R G A N I C J Q A
D P H J I B Z A X B S
E U T L D O X S P F H
C W E B S I T E H V T
K J Q U P A L S P C A
L W M A R K E T I N G
U H E S I F H U T Z F
T K D N A Y Q D C T C
Z G I E M L D Y H L X
J Y A U K P E K S E O
'''
clues = ['MARKETING', 'CASESTUDY', 'ORGANIC', 'PAID',
            'PITCH', 'SEO', 'HASHTAG', 'CTC', 'WEBSITE', 'DECK', 'MEDIA', 'SALE']
   
puzzle = puzzle.replace(' ','')            
length = puzzle.index('\n')+1
#Make a list of tuples containing each letter and its row and column
letters = [(letter, divmod(index, length))
            for  index, letter in enumerate (puzzle)]
#Reorder the list to represent each reading direction,
#and add them all to a dictionary
lines = {}
offsets = {'down':0, 'right down':-1, 'left down':1}
for direction, offset in offsets.items():
    lines[direction] = []
    for i in range(length):
        for j in range(i, len(letters), length + offset):
            lines[direction].append(letters[j])
        lines[direction].append('\n')
lines['left']  = letters
lines['right'] = [i for i in reversed(letters)]
lines['up'] = [i for i in reversed(lines['down'])]
lines['left up'] = [i for i in reversed(lines['right down'])]
lines['right up'] = [i for i in reversed(lines['left down'])]
#Make strings from the letters, find the words in them and retrieve
#their original locations
for direction, tup in lines.items():
    string = ''.join([i[0] for i in tup])
    for word in clues:
        if word in string:
            location = tup[string.index(word)][1]
            print(word, 'row', location[0]+1, 'column', location[1]+1, direction)


#show word outline
import cv2
img = cv2.imread('getjob.png',0)
cv2.imshow('image',img)

