def solution(players, callings):
    dic = {}
    for i in range(len(players)):
        dic[players[i]] = i
    length = len(callings)
    for i in range(length):
        caller = callings[i]
        callIdx = dic[caller]
        before = players[callIdx-1]
        beforeIdx = dic[before]
        players[callIdx-1], players[callIdx] = players[callIdx], players[callIdx-1]
        dic[caller] -= 1
        dic[before] += 1
        
    return players

    #시간초과: n제곱
    # length = len(callings)
    # for i in range(length):
    #     callIdx = players.index(callings[i])
    #     players[callIdx-1], players[callIdx] = players[callIdx], players[callIdx-1]
    # return players        