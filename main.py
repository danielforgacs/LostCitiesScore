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
    # rounds = ['p1-r1', 'p2-r1']

    # for round_ in rounds:
    #     print(round_)
    #     scoretext = input('score: ')
    #     # print(counter.main(text=scoretext))

    #     # scoretext = input('score: ')

    p1score = 0
    p2score = 0

    scoretext = input('Player 1 cards: ')
    p1score += counter.main(text=scoretext)

    scoretext = input('\nPlayer 2 cards: ')
    p2score += counter.main(text=scoretext)

    print('.'*79)

    scoretext = input('Player 1 cards: ')
    p1score += counter.main(text=scoretext)

    scoretext = input('\nPlayer 2 cards: ')
    p2score += counter.main(text=scoretext)

    print('.'*79)

    scoretext = input('Player 1 cards: ')
    p1score += counter.main(text=scoretext)

    scoretext = input('\nPlayer 2 cards: ')
    p2score += counter.main(text=scoretext)

    print('-'*79)

    print('Player 1 score total: {}'.format(p1score))
    print('Player 2 score total: {}'.format(p2score))
