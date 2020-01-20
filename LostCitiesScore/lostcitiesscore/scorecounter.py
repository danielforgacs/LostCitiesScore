import os
import sys
import re

ROOTDIR = (
    os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
)))

sys.path = [ROOTDIR] + sys.path

import lostcitiesscore.settings as settings




# VALID_SCORES = r'[dt123456789]+'
# VALID_SCORES = r'[d\*t123456789 ]{1,5}'
VALID_SCORES = r'd{1,3}'






def is_valid_score(txt):
    is_valid = False
    check = re.fullmatch(VALID_SCORES, txt)

    if check:
        is_valid = True

    # if not txt:
    #     is_valid = False



    return is_valid





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
