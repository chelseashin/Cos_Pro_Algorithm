# 1번 문제(5분)
# 14:03 ~ 14:08
def solution1(temperature, A, B):
    A_temp, B_temp = temperature[A], temperature[B]
    result = 0
    for temp in temperature:
        if (temp > A_temp and temp > B_temp):
            result += 1
    return result

print("#1", solution1([3, 2, 1, 5, 4, 3, 3, 2], 1, 6))

# 2번 문제(5분)
# 14:10 ~ 14:15
def solution2(papers, papers_len, K):
    result = 0
    for paper in papers:
        if paper <= K:
            K -= paper
            result += 1
        else: break
    return result

print("#2", solution2([2, 4, 3, 2, 1], 5, 10), solution2([2, 4, 3, 2, 1], 5, 14))

# 3번 문제(5분)
# 14:18 ~ 14:23
def solution3(people):
    result = []
    for size in people:
        if size < 95: result.append("S")
        elif (95 <= size < 100): result.append("M")
        elif (100 <= size < 105): result.append("L")
        else: result.append("XL")
    return result

print("#3", solution3([97, 102, 93, 100, 107]))

# 4번 문제(15분)
# 14:24 ~ 14:41
def solution4(cards):
    total = 0
    card_info = set()
    for color, num in cards:
        total += int(num)
        card_info.add(color)
    # print("card_info", card_info, len(card_info))
    if len(card_info) == 3:
        return total
    elif len(card_info) == 2:
        return total * 2
    else: return total * 3

print("#4", solution4([["blue", "2"], ["red", "5"], ["black", "3"]]), solution4([["blue", "2"], ["blue", "5"], ["black", "3"]]))

# 5번 문제
# 가장 까다로웠던 문제 - 차근차근 생각하면 풀 수 있다!
def solution5(money, price, n):
    bottle = money // price     # 최초로 구매한 음료수 갯수
    result = bottle             # 마실 수 있는 음료수의 총합
    while bottle >= n:
        remain = bottle % n     # 나머지
        bottle //= n            # 빈 병 교환(몫)
        result += bottle
        bottle += remain        # 다음 
        # print("마신 후 상태", result, bottle)
    return result

print("#5", solution5(8, 2, 4), solution5(6, 2, 2))
# print("#5", )


# 6번 문제(15분)
# 09:23 ~ 09:38
def solution6(password):
    # print("A-Z", ord("A"), ord("Z"))
    # print("a-z", ord("a"), ord("z"))
    # print("0-9", ord("0"), ord("9"))
    upper, lower, digit = False, 0, 0
    for word in password:
        # print("아스키코드 변환", word, ord(word))
        if 65 <= ord(word) <= 90:       # 대문자 확인
            upper = True
        elif 97 <= ord(word) <= 122:    # 소문자 확인
            lower += 1
        elif 48 <= ord(word) <= 57:     # 숫자 확인
            digit += 1
    if upper and (lower >= 2) and (digit >= 2):
        return "true"
    return "false"

print("#6", solution6("helloworld"), solution6("Hello123"))


# 7번 문제
# 09:39 ~ 09:46
def solution7(money, chairs, desks):
    maxValue = 0
    for chair in chairs:
        for desk in desks:
            temp = chair + desk
            if (temp <= money and temp > maxValue):
                maxValue = temp
    return maxValue

print("#7", solution7(7, [2, 5], [4, 3, 5]), solution7(7, [3], [5]))


# 8번 문제
# 09:47 ~ 09:59
def solution8(number):
    revnum = int(''.join(list(str(number))[::-1]))
    return abs(number-revnum)

print("#8", solution8(120), solution8(23))


# 9번 문제
# 10:16 ~ 10:23
def solution9(socks):
    result = 0
    info = {}
    for color in socks:
        if color not in info.keys():
            info[color] = 1
        else: 
            info[color] += 1
            if info[color] and (info[color] % 2 == 0):
                result += 1
    return result

print("#9", solution9([1, 2, 1, 3, 2, 1]))


# 10번 문제
# 10:25 ~ 10:29
def solution10(weight, boxes):
    result = 0
    minWeight, maxWeight = weight * 0.9, weight * 1.1
    for box in boxes:
        if not (minWeight <= box <= maxWeight):
            result += 1
    return result

print("#10", solution10(600, [653, 670, 533, 540, 660]))