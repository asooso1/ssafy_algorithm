import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def match(l,r):
    if cards[l] - cards[r] == -2 or cards[l] - cards[r] == 1 or cards[l] - cards[r] == 0:
        return l
    else:
        return r

def half(s,e):
    if s == e:   # s와 e가 같다는건 번호가 같은거니까 동일한 사람 지칭
        return s
    m = (s+e)//2
    left = half(s, m)
    right = half(m+1, e)
    return match(left, right)


for tc in range(1,T+1):
    N = int(input())
    cards = list(map(int,input().split()))

    print('#{} {}'.format(tc, half(0,N-1)+1))
