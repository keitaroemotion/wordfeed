#!/usr/bin/env python3
#

# first argument is the amount of the text

import random
import sys

args = sys.argv[1:len(sys.argv)]

if(len(args) < 1):
    print("args missing.")
    sys.exit()

text_amount = int(args[0])

word_list = ['is', 'am', 'good', 'goose', 'better', 'blockchain', 'sunny', 'height', 'mostly', 'bitter', 'type', 'canon', 'creed', 'hype', 'right', 'left', 'in', 'out', 'nasty']

text = ''

while len(text) < text_amount:
    i = random.randint(0, len(word_list)-1)
    text += word_list[i] + ' '

def fit(text, text_amount):
    if(len(text) < text_amount):
        return fit(text + '.', text_amount)
    return text[:text_amount]

print(fit(text, text_amount))
