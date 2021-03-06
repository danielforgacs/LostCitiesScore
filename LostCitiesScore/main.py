import os
import sys

ROOTDIR = (
    os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
)))

sys.path = [ROOTDIR] + sys.path

import LostCitiesScore.scorecounter as counter




def main():
    player_one = 0
    player_two = 0

    rounds = range(1, 4)

    for rnd in rounds:
        print()
        print('.'*79)
        print('Round: {}'.format(rnd))

        scoretext = input('\tPlayer 1 cards: ')
        roundscore = counter.PlayerRows(text=scoretext).value
        player_one += roundscore
        print('\t   round score: {}'.format(roundscore))
        print('\t   total score: {}'.format(player_one))

        print()

        scoretext = input('\tPlayer 2 cards: ')
        roundscore = counter.PlayerRows(text=scoretext).value
        player_two += roundscore
        print('\t   round score: {}'.format(roundscore))
        print('\t   total score: {}'.format(player_two))

        print('\tscore diff: {}'.format(abs(player_two-player_one)))

    print()
    print('-'*79)
    print('Total:')
    print('player one total: {}'.format(player_one))
    print('player two total: {}'.format(player_two))



if __name__ == '__main__':
    main()
