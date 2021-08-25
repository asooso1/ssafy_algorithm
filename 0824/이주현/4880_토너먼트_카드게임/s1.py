import sys
sys.stdin = open('sample_input.txt', 'r')
'''
1: 가위
2: 바위
3: 보
'''
def result(i, j):
    if member[i] == member[j]:
        return i
    elif member[i] == 1: # i = 가위
        return j if member[j] == 2 else i
    elif member[i] == 2: # i = 바위
        return i if member[j] == 1 else j
    elif member[i] == 3: # i = 보
        return j if member[j] == 1 else i

def match(i, j):
    if j - i < 1:
        return i
    elif j - i + 1 == 2:
        return result(i, j)
    else: # 3명 이상일 때
        return result(match(i, (i+j)//2), match(((i+j)//2) + 1, j))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    member = list(map(int, input().split()))

    print("#{} {}".format(tc, match(0, len(member) - 1)+1))