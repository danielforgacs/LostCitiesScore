import os
import sys

ROOTDIR = (
    os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
)))

sys.path = [ROOTDIR] + sys.path

import LostCitiesScore.settings as settings



class ValueDescriptor:
    def __set__(self, obj, value):
        if not value in range(2, 11):
            raise ValueError('BAD CARD VALUE')
        obj.__dict__['value'] = value

    def __get__(self, obj, objtype):
        return obj.__dict__['value']


class Card_OLD:
    value = ValueDescriptor()

    def __init__(self, value):
        self.value = value




class Card:
    def __init__(self, value):
        if not value in range(2, 11):
            raise ValueError('BAD CARD VALUE')
        self.value = value





def count_colour(scoretext):
    multiplier = 1
    cardcount = len(scoretext)
    cards = []

    for item in scoretext:
        if item == 'd':
            card = None
            multiplier += 1
        elif item in settings.TEN_TOKENS:
            card = Card(value=10)
        else:
            card = Card(value=int(item))

        cards.append(card)

    cards = filter(bool, cards)
    totalscrore = sum(map(lambda x: x.value, cards))
    totalscrore -= 20
    totalscrore *= multiplier

    if cardcount >= 8:
        totalscrore += 20

    return totalscrore





def count_colour_OLD(scoretext):
    totalscrore = -20
    multiplier = 1
    cardcount = len(scoretext)

    for item in scoretext:
        if item == 'd':
            multiplier += 1
        elif item in settings.TEN_TOKENS:
            totalscrore += 10
        else:
            totalscrore += int(item)

    totalscrore *= multiplier

    if cardcount >= 8:
        totalscrore += 20

    return totalscrore



def main(text):
    scoretexts = text.split(settings.COLOUR_SEPARATOR)

    score = 0

    for txt in scoretexts:
        subscore = count_colour(scoretext=txt)
        print('\t\tsubcount: {} - cardcount: {}'.format(subscore, len(txt)))
        score += subscore

    return score







if __name__ == '__main__':
    pass
