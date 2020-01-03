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

    rounds = ['p1-r1', 'p2-r1']

    for round_ in rounds:
        print(round_)
        scoretext = input('score: ')
        # print(counter.main(text=scoretext))

        # scoretext = input('score: ')
