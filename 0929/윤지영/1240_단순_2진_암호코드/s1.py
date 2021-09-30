import sys
sys.stdin = open('input.txt')

check = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5,
         '0101111':6, '0111011':7, '0110111':8, '0001011':9}


def find_start():
    for i in range(N):
        for j in range(M-1,-1,-1):
            if board[i][j] == '1':
                return [i,j]

def vaild(n):
    ans_2 = ans_1 = 0
    # 문제에선 홀수자리의 합이지만 인덱스가 0부터 시작이므로 짝수자리의 합 x 3 + 홀수자리합 + 검증코드로 작성
    for i in range(len(n)-1):
        if i % 2 == 0 :
            ans_2 += n[i]
        else:
            ans_1 += n[i]
    ans = ans_2 * 3 + ans_1 + n[-1]
    if ans % 10 ==0:
        return True
    else:
        return False



T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    board = [input() for _ in range(N)]
    num = [[] for _ in range(8)]
    c = 0
    start = find_start()
    for k in range(start[1], start[1]-56, -7):
        num[c] = board[start[0]][k-6:k+1]
        c += 1
    # 뒤에서부터 집어넣었으므로 전체 순서 다시 뒤집기
    num.reverse()
    result = []
    for n in num:
        result.append(check[n])
    if vaild(result) is True:
        ans = sum(result)
    else:
        ans = 0


    print('#{} {}'.format(tc,ans))












# 암호코드가 처음부터 시작한다는 가정 하에 짠 코드
# for tc in range(1,T+1):
#     N,M = map(int,input().split())
#     code = [[[] for _ in range(M // 7)] for _ in range(N)]
#     for i in range(N):
#         li = input()
#         j = 0
#         for k in range(0,M-6,7):
#             code[i][j] = li[k:k+7]
#             j += 1
#
#     print(code)
