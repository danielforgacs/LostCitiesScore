import os
import sys

ROOTDIR = (
    os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
)))

sys.path = [ROOTDIR] + sys.path

import LostCitiesScore.scorecounter as counter



if __name__ == '__main__':
    scoretext = input('score: ')

    while scoretext:
        print(counter.main(text=scoretext))

        scoretext = input('score: ')
