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
# 14:41 ~ 

def solution5(money, price, n):
    result = 0      # 마실 수 있는 음료수의 총합
    while :

        
        print("마신 후 상태", result, money, price)
        
    return result

print("#5", solution5(8, 2, 4))
print("========================================================")
print("#5", solution5(6, 2, 2))