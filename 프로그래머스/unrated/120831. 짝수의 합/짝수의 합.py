def solution(n):
    num = []
    for i in range(1,n+1):
        if(i % 2 == 0):
            num.append(i)
    return sum(num)