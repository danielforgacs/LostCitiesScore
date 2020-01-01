scoretext = 'ddd234567891'
scoretext = 'd'
scoretext = 'd1'
scoretext = '2'
scoretext = '23'
scoretext = 'd23'
scoretext = 'ddd234681'
scoretext = '281;281'
scoretext = 'd281;dd281'
scoretext = '291'
scoretext = '291;291'
scoretext = 'd291;291'
scoretext = 'd291;d291'




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






if __name__ == '__main__':
    # scoretexts = scoretext.split(';')
    # print(scoretexts)
    scoretext = input('score: ')
    scoretexts = scoretext.split(';')
    print(scoretexts)

    score = 0

    for txt in scoretexts:
        score += count_colour(scoretext=txt)

    print(score)
