def count_colour(scoretext):
    totalscrore = -20
    multiplier = 1
    cardcount = len(scoretext)

    for item in scoretext:
        if item == 'd':
            multiplier += 1
        elif item == '1':
            totalscrore += 10
        else:
            totalscrore += int(item)


    totalscrore *= multiplier

    if cardcount >= 8:
        totalscrore += 20

    print('subcount: {} - cardcount: {}'.format(totalscrore, cardcount))

    return totalscrore



def main(text):
    scoretexts = text.split(';')

    score = 0

    for txt in scoretexts:
        score += count_colour(scoretext=txt)

    return score







if __name__ == '__main__':
    print(2+3+4+5+6+7+8+9+10)
    print(count_colour(scoretext='234567891'))
    print(count_colour(scoretext='281'))
    print(main(text='234567891'))

    assert count_colour(scoretext='2345678') == -20+2+3+4+5+6+7+8
