import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def bfs(s,v):
    q = []          # 큐 생성
    q.append(s)     # 시작점 인큐    #enQ
    si , sj = s[0], s[1]
    visited[si][sj] = 1  # 시작점 방문표시
    while q:
        t1, t2 = q.pop(0)    # 큐에서 하나 꺼내서 t에 저장 #deQ
        for w in adjList[t1][t2]:       # 갈 수 있는 곳 w 순회
            w1,w2 = w[0],w[1]
            if visited[w1][w2] == 0:    # 미방문했다면
                if w == v:
                    return visited[t1][t2] - 1      # 도착지 바로 전까지만 세야 하므로 -1
                else:
                    q.append(w)             # 정점 인큐
                    visited[w1][w2] = visited[t1][t2] + 1
    return 0


for tc in range(1,T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    adjList = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                s = [i,j]               # 시작점 인덱스
            elif maze[i][j] == '3':
                e = [i,j]               # 도착점 인덱스
    di = [1,-1,0,0]
    dj = [0,0,1,-1]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if maze[ni][nj] != '1':
                        adjList[i][j].append([ni,nj])

    print('#{} {}'.format(tc, bfs(s,e)))