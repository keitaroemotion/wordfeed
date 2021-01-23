#!/usr/bin/env python3
#

# first argument is the amount of the text

import random
import sys

args = sys.argv[1:len(sys.argv)]

if(len(args) < 1):
    print("args missing.")
    sys.exit()

max_width = 100

text_amount = int(args[0])

word_sample = "For all the fanfare made when Prime Minister Boris Johnson struck a trade deal with Brussels on Christmas Eve, the inescapable reality of leaving the European Union's customs and regulatory territory has already started to bite. The fact that the deal was only agreed one week before it came into effect meant that dangerous disruption to countless businesses that relied on seamless supply chains was inevitable. Despite Johnson's repeated claims that Brexit is a great opportunity for British exporters and would lead to some kind of revival for free trade, the reality is very different: freshly caught fish are reportedly being left to rot as exporters cannot get them to the European Union while logistics firms are skeptical that both importing and exporting is going to be viable for many businesses in the long term. Fallout from Brexit and the coronavirus pandemic is pushing the UK economy into a sharp contraction in the first quarter, according to data published Friday by IHS Markit, meaning a double-dip recession is now on the cards.  While it should be a source of embarrassment for the PM that his deal has made life very difficult for many of the industries that he has championed post-Brexit, Johnson's public statements on the matter suggest he is oblivious to the reality that many are facing.  Scottish fishermen say Brexit carnage threatens to kill their business Scottish fishermen say 'Brexit carnage' threatens to kill their business When asked for comment on the immediate consequences of the trade barriers implemented as a result of the deal, a UK government spokesperson told CNN Business: From the outset we were clear that we would be leaving the customs union and single market which meant that there would be new processes after the end of the Transition Period. These were widely communicated through our public information campaign. The starkest example of what Brexit is doing to British business comes from Scotland's fishing industry. Despite the government's claims during Brexit negotiations that the fishing industry was very near the top of its priority list, there is a real fear that the entire industry could collapse in a matter of weeks.  We had an entirely new system for exporters to get their heads around that hadn't been tested prior to use. The result, somewhat inevitably, was that it started going wrong straight away, says James Withers, chief executive of Scotland Food and Drink. This isn't as simple as an IT glitch that needs fixing. In a matter of days, we went from being able to send fresh food to Madrid with a single cover sheet of paperwork. Now there are roughly 26 steps for each transaction."

word_list = word_sample.split(' ')

text = ''

width = 0
while len(text) < text_amount:
    i = random.randint(0, len(word_list)-1)
    text += word_list[i] + ' '
    width += (len(word_list[i]) + 1)
    if(width > max_width):
        text = text + '\n'

def fit(text, text_amount):
    if(len(text) < text_amount):
        return fit(text + '.', text_amount)
    return text[:text_amount]

print(fit(text, text_amount))
