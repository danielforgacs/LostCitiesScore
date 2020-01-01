scoretxt = 'ddd234567891'
# scoretxt = 'd'
# scoretxt = 'd1'

totalscrore = 0
multiplier = 1

for item in scoretxt:
    if item == 'd':
        multiplier += 1
    elif item == '1':
        totalscrore += 10
    else:
        totalscrore += int(item)


totalscrore *= multiplier

print(totalscrore)
