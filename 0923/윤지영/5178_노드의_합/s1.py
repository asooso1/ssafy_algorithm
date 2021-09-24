import sys
sys.stdin = open('5178_sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    node = [0] * (N+1)
    for k in range(M):
        idx, n = map(int,input().split())
        node[idx] = n
    for m in range(N//2,0,-1):
        if node[m]==0:
            if (m*2 <= N) and (m*2+1 <=N):
                node[m] = node[m*2] + node[m*2+1]
            elif m*2+1 > N:
                node[m] = node[m*2]
    print('#{} {}'.format(tc, node[L]))
    
