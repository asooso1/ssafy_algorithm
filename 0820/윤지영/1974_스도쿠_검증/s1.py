import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1,T+1):
    board = [list(map(int, input().split())) for _ in range(9)]
    ans = 1
    for i in range(9):
        used_row = [0] * 10         # 열 하나 순회 끝날때마다 초기화
        used_col = [0] * 10         # 행 하나 순회 끝날때마다 초기화
        for j in range(9):
            num = board[i][j]           # 해당 칸의 숫자를 num에 저장
            if used_col[num] == 0:      # used_col, 즉 행 숫자 체크 배열에서 해당 숫자 체크했는지 확인
                used_col[num] = 1
            else:
                ans = 0
                break
            num = board[j][i]
            if used_row[num] == 0:      # used_row, 즉 열 숫자 체크 배열에서 해당 숫자 체크했는지 확인
                used_row[num] = 1
            else:
                ans = 0
                break
            if (not i % 3) and (not j % 3):     # 바둑판모양 인덱스는 (0,0), (0,3), (0,6), (3,0) ... 으로 3의 배수이므로
                used_3 = [0] * 10           # 3 x 3 하나 순회 끝날때마다 초기화
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = board[r][c]
                        if used_3[num] == 0:
                            used_3[num] = 1
                        else:
                            ans = 0
                            break
    print('#{} {}'.format(tc, ans))


