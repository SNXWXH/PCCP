def solution(players, callings):
    # {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
    pla_dic = {key: idx for idx, key in enumerate(players)}
    
    for p in callings:
        c = pla_dic[p]
        pla_dic[p] -= 1
        pla_dic[players[c-1]] += 1
        players[c-1], players[c] = players[c], players[c-1]

    return players

    #시간초과: n제곱
    # length = len(callings)
    # for i in range(length):
    #     callIdx = players.index(callings[i])
    #     players[callIdx-1], players[callIdx] = players[callIdx], players[callIdx-1]
    # return players        