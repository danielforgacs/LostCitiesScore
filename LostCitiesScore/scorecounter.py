import os
import sys

ROOTDIR = (
    os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
)))

sys.path = [ROOTDIR] + sys.path

import LostCitiesScore.settings as settings




class Card:
    def __init__(self, value):
        if value not in range(2, 11):
            raise ValueError('BAD CARD VALUE')
        self.value = value




class ColourRow:
    def __init__(self, scoretext):
        self.scoretext = scoretext


    @property
    def value(self):
        multiplier = 1
        cardcount = len(self.scoretext)
        cards = []

        for item in self.scoretext:
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





class PlayerRows:
    def __init__(self, text):
        not_text = not bool(text)
        not_string = not isinstance(text, str)
        not_validchar = lambda x: x not in settings.VALID_CHARS
        is_wrongchars = any(map(not_validchar, str(text)))

        if not_text or not_string or is_wrongchars:
            raise ValueError('BAD PLAYER TEXT')

        self.text = text


    @property
    def value(self):
        scoretexts = self.text.split(settings.COLOUR_SEPARATOR)
        score = 0

        for txt in scoretexts:
            subscore = ColourRow(scoretext=txt).value
            print('\t\tsubcount: {} - cardcount: {}'.format(subscore, len(txt)))
            score += subscore

        return score





if __name__ == '__main__':
    pass
