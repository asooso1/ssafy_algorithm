import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    words = []
    max_words = 1
    for _ in range(5):
        k = input()
        if max_words < len(k):       # 단어의 최대 길이 찾기
            max_words = len(k)
        words.append(k)
    for i in range(5):
        if len(words[i]) < max_words:   # 해당 케이스의 최대 길이보다 짧은 단어는
            words[i] = words[i] + '/'*(max_words - len(words[i]))   # 절대 안나올 '/'로 공백 표시
    stack = []
    for i in range(max_words):
        for j in range(5):
            if words[j][i] == '/':    # 공백표시는 넘어가기
                continue
            stack.append(words[j][i])
    print('#{} {}'.format(tc, ''.join(stack)))
