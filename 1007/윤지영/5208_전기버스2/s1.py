import sys
sys.stdin = open('sample_input (1).txt')

def dfs(now_bus,cnt):
    global min_cnt, N
    if cnt > min_cnt :
        return
    if now_bus >= N-1:
        return
    # 현재 정류장번호가 도착점이라면 최솟값 갱신
    # 현재 번호에서 갈수 있는 정류장이 도착지점을 넘어선다면, 끝까지 갈 수 있는 것이므로 종료!!!
    if now_bus + battery_list[now_bus] >= N-1:
        if min_cnt > cnt :
            min_cnt = cnt
            return
    # 아직 도착점에 도착하지 않았다면
    elif now_bus < N-1:
        for i in range(1, battery_list[now_bus]+1):
            now_bus += i
            dfs(now_bus, cnt+1)
            now_bus -= i

T = int(input())
for tc in range(1,T+1):
    li = list(map(int,input().split()))
    N, battery_list = li[0], li[1:]
    # 정류장은 최대 100개이므로 교환횟수는 1000을 넘지 않을것
    min_cnt = 1000
    dfs(0,0)
    print('#{} {}'.format(tc, min_cnt))