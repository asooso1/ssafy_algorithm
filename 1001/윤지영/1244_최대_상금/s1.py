import sys
sys.stdin = open('input.txt')

def find_big(li,n,small):
    max_idx = n-1
    for k in range(n-1,small,-1):
        if board[max_idx] < board[k]:
            max_idx = k
    return max_idx

def find_small(li,n,big):
    min_idx = 0
    for j in range(big):
        if board[min_idx] > board[j]:
            min_idx = j
    return min_idx


T = int(input())
for tc in range(1,T+1):
    N = list(input().split())
    trade = int(N[-1])
    board = list(N[0])
    n = len(board)
    # 뒤에서 찾을땐 가장 큰수, 앞에서 찾을땐 가장 작은수 -> 그렇게 교환
    b, s = n,0
    # 교환 횟수가 남아있다면
    while trade:
        # 탐색 시작지점 s가 마지막인덱스가 아니라면
        if s <= n-1:
            # 뒤에서부터 s까지 탐색하면서 가장 큰 값찾기 -> 큰 값은 앞에 있을 수록 좋으므로, 가장 뒤에 있는 값을 옮기기 위해서
            b = find_big(board,n,s-1)
            # 가장 큰 값이 숫자판에서 중복없이 있다면
            if board.count(board[b]) == 1:
                # 찾은 값의 인덱스가 현재 시작지점과 같지 않다면
                if s != b :
                    # 교환, 교환횟수 - 1, 시작지점 +1
                    board[b], board[s] = board[s], board[b]
                    trade -= 1
                    s += 1
                # 찾은 값이 인덱스가 현재 시작지점과 같다면, 교환해봤자 제자리걸음이므로 교환없이 시작지점만 + 1
                else:
                    s += 1
            # 가장 큰 값이 숫자판에서 중복이라면
            else:
                # 맨 앞에서부터 해당 값의 인덱스까지만 탐색하면서 가장 작은 값 찾기 -> 작은 값은 뒤에 있을 수록 좋으므로 가장 앞에 있는 작은 값을 옮기기 위해서
                m = find_small(board, n, b)
                # 가장 작은 값과 찾은 큰 값 교환 , 교환 횟수 - 1
                board[m], board[b] = board[b], board[m]
                trade -= 1
        # 탐색 시작지점 s가 마지막인덱스라면, 크기에따른 교환은 모두 끝낸것이므로 교환횟수를 모두 소모할때까지 제일 작은 값들인 마지막 두 값을 무한히 교환
        else:
            board[n-1], board[n-2] = board[n-2], board[n-1]
            trade -= 1

    print('#{} {}'.format(tc, ''.join(board)))



