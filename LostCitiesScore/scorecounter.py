import os
import sys

ROOTDIR = (
    os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
)))

sys.path = [ROOTDIR] + sys.path

import LostCitiesScore.settings as settings






def count_colour(scoretext):
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

    print('\t\tsubcount: {} - cardcount: {}'.format(totalscrore, cardcount))

    return totalscrore



def main(text):
    scoretexts = text.split(settings.COLOUR_SEPARATOR)

    score = 0

    for txt in scoretexts:
        score += count_colour(scoretext=txt)

    return score







if __name__ == '__main__':
    pass
