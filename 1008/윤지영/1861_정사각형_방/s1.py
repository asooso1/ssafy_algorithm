import sys
sys.stdin = open('input.txt')

# 다른방법 1 -> 1번에서 2번으로 갈 수 있으면 배열[1] =1 , 3번에서 4번으로 갈 수 있으면 배열[3] = 1 .. 이런식으로 배열을 하나 만들고,
# 뒤에서부터 순회하면서 1이나오면, 0이 나올때까지 cnt +1 -> 최대값보다 크거나 같으면 최대값 갱신하고 마지막으로 1이 나온 번호를 i에 저장하고, 갈 수 있는 방 갯수는, 본인 방도 포함해야하므로 cnt += 1
# 뒤에서부터 순회하므로 최대값이 같더라도, 순회끝나면 그 중 작은 번호가 i에 저장되게 됨


# 다른방법 2 -> 2차원배열을 뒤에서부터 순회하면서 pos배열에 각 방번호의 좌표(i,j) 추가 -> dis =[1]*(N*N+1) 로 1로 초기화
# 그러면 pos[1]은 1번 방의 좌표 등이 들어갈 것이고, pos 배열을 순회하면서 (1번방 좌표에서 2번방 좌표가 상하좌우로 갈 수있는 경우라면
# 즉, 두 방 좌표의 차이가 (1,0), (0,1), (-1,0), (0,-1) 안에 존재한다면, 갈 수 있는 것이므로 dis[i-1] = dis[i]+1 (다음 방번호의 거리 + 1)만큼 추가 (뒤에서부터 순회하므로)
# 그러면서 최대값보다 dis[i-1]가 더 크다면, 최댓값을 갱신하고, 방번호도 갱신



def check(i,j):
    global cnt
    # 22번 케이스 200*200개 출력하려면 가지치기 필요..어떻게 해야하려나

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if board[i][j] + 1 == board[ni][nj]:
                cnt += 1
                check(ni,nj)
    return



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    #    우 하 좌 상
    max_cnt = 0
    max_idx = 987654321
    for i in range(N):
        for j in range(N):
            # 현재 방 1개에서 시작
            cnt = 1
            check(i,j)
            if max_cnt == cnt:
                if max_idx > board[i][j]:
                    max_idx = board[i][j]
            if max_cnt < cnt:
                max_cnt = cnt
                max_idx = board[i][j]

    print('#{} {} {}'.format(tc,max_idx, max_cnt))
