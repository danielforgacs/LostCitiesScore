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
    player_one = 0
    player_two = 0

    rounds = range(1, 4)

    for rnd in rounds:
        print()
        print('.'*79)
        print('Round: {}'.format(rnd))

        scoretext = input('\tPlayer 1 cards: ')
        player_one += counter.main(text=scoretext)

        print()

        scoretext = input('\tPlayer 2 cards: ')
        player_two += counter.main(text=scoretext)

    print()
    print('-'*79)
    print('Total:')
    print('player one total: {}'.format(player_one))
    print('player two total: {}'.format(player_two))
