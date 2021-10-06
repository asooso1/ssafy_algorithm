import sys
sys.stdin = open('input.txt')

def perm(n,m,k):
    global arr, p
    if k == n:
        if p[0] == 1:
            start.append(p[:])
        elif p[1] ==1:
            end.append(p[:])
        else:
            li.append(p[:])
    else:
        for i in range(m):
            if not used[i]:
                p[k] = arr[i]
                used[i] = 1
                perm(n,m,k+1)
                used[i] = 0

def search(cnt, sta, add):
    global ans
    si,sj = sta

    if cnt == N-1:
        add += board[sj][1]
        if ans > add:
            ans = add
        return
    else:
        for l in li:
            if l[0] == sj and not used[l[1]]:
                ls,le = l
                if board[ls][le] != 0 :
                    temp = board[ls][le]
                    board[ls][le] = 0
                    used[ls] = 1
                    search(cnt+1, l, add + temp)
                    board[ls][le] = temp
                    used[ls] = 0

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [[0] * (N+1)] + [[0] + list(map(int,input().split())) for _ in range(N)]
    used = [0]*(N+1)
    arr = list(range(1,N+1))
    li = []
    end = []
    start = []
    p = [0] * 2
    ans = 9999999999999
    perm(2,N,0)
    used = [0] * (N+1)
    for s in start:
        si, sj = s
        a = board[si][sj]
        board[si][sj] = 0
        search(1, s, a)
    print('#{} {}'.format(tc,ans))




