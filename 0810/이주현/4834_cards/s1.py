import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cards = input()
    count = [0]*10

    #카드 수 세기기
    for idx in range(len(cards)):
       count[int(cards[idx])] += 1

    max_count = count[0]
    max_index = 0

    #최대 장수, 숫자 구하기
    for idx in range(1, len(count)):
        if max_count <= count[idx]:
            max_count = count[idx]
            max_index = idx

    print("#{} {} {}".format(test_case, max_index, max_count))