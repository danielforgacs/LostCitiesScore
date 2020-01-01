def count_colour(scoretext):
    totalscrore = -20
    multiplier = 1
    count = 0

    for count, item in enumerate(scoretext):
        if item == 'd':
            multiplier += 1
        elif item == '1':
            totalscrore += 10
        else:
            totalscrore += int(item)


    totalscrore *= multiplier

    if count > 7:
        totalscrore += 20

    return totalscrore



def main(text):
    scoretexts = text.split(';')

    score = 0

    for txt in scoretexts:
        score += count_colour(scoretext=txt)

    return score







if __name__ == '__main__':
    # scoretexts = scoretext.split(';')
    # print(scoretexts)
    scoretext = input('score: ')

    print(main(text=scoretext))
