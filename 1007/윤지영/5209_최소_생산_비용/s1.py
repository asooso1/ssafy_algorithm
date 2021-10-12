import sys
sys.stdin = open('sample_input (1).txt')

def perm(n,k,ans):
    global min_cost
    if ans > min_cost:
        return
    if k == n:
        if ans < min_cost:
            min_cost = ans
    else:
        for i in range(n):
            if not used[i]:
                p[k] = arr[i]
                used[i] = 1
                perm(n,k+1, ans+cost[k][p[k]])
                used[i] = 0


T= int(input())
for tc in range(1,T+1):
    N = int(input())
    cost = [list(map(int,input().split())) for _ in range(N)]
    p = [0] * N
    arr = [i for i in range(N)]
    used = [0] * (N+1)
    min_cost = 99 * (N ** 2)
    perm(N,0,0)
    print('#{} {}'.format(tc,min_cost))



