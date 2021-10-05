import sys
sys.stdin = open('input.txt')

def search(n, li, start, end, add):
    global ans
    si,sj = start
    ei,ej = end

    if ans < add + li[ei][ej]:
        return
    if si == n-1 and sj == n-1:
        if ans > add:
            ans = add
        return

    else:
        for k in range(2):
            ni = si + di[k]
            nj = sj + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                val = li[ni][nj]
                if val != -1:
                    add += val
                    li[ni][nj] = -1
                    search(n,li,[ni,nj],end,add)
                    li[ni][nj] = val
                    add -= val

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    di = [0,1]     # 상 하
    dj = [1,0]      # 우 좌
    ans = 9999999999999999999
    init = board[0][0]
    board[0][0] = -1
    search(N,board[:], [0,0], [N-1,N-1], init)
    print('#{} {}'.format(tc,ans))
