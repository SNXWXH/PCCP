from collections import Counter

def solution(participant, completion):
    cntPart = Counter(participant)
    cntComp = Counter(completion)
    
    person = cntPart - cntComp
    
    first_key = next(iter(person))
    return first_key
    
    # 효율성 시간초과
    # parLength = len(participant)
    # for i in range(parLength):
    #     cntPar = participant[i]
    #     if cntPar not in completion:
    #         return cntPar
    #     else:
    #         completion.pop(completion.index(cntPar))
    #         print(cntPar)