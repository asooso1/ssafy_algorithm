import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1,T+1):
    N = int(input())  # 농장 크기
    field = [list(map(int, input())) for _ in range(N)]
    benefit = 0
    m = 1
    j = (N-1)//2
    if N > 1:
        for i in range(j+1):
            j_s = j - i
            j_e = j + i
            for r in range(j_s, j_e+1):
                benefit += field[i][r]
        for i in range(j+1, N):
            k = i - (2*m)
            j_s = j - k
            j_e = j + k
            m += 1
            for r in range(j_s, j_e+1):
                benefit += field[i][r]
    else:
        benefit = field[0][0]
    print('#{} {}'.format(tc, benefit))