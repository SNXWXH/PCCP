def solution(numbers):
    sum = 0
    length = len(numbers)
    for i in range(length):
        sum += numbers[i]
    return sum / length