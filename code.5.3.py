name = []
fen1 = []
fen2 = []
sname = ''

while not sname == 'game over':
    if len(name) >1 and name[0] == name [1]:
        name.pop(0)
    else:
        sname = input('得分球队：')
        name.append(sname)
        if name[0] == sname:
            sfen = int(input('得分：'))
            fen1.append(sfen)
            a1 = sum(fen1)
        elif name[1] == sname:
            sfen = int(input('得分：'))
            fen2.append(sfen)
            a2 = sum(fen2)
else:
    print('比赛结束')
    if a1 > a2:
        print('winner is:',name[0])
    elif a1 < a2:
        print('winner is:',name[1])
    else:
        print('Draw')
