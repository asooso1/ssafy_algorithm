import sys
sys.stdin = open("s_input.txt")

#1.모든 노선 체크
def bus_count(bus_stop):
    cnt = 0

    for i in range(N):
        if bus_route[i][0] <= bus_stop <=bus_route[i][1]:
            cnt +=1
    return cnt

T = int(input())
f    or tc in range(1, T + 1):
    N = int(input())  # 버스 노선 수

    bus_route = []

    for i in range(N):
        A,B = map(int,input().split())
        bus_route.append((A,B))
    #내가 확인하고 싶은 정류장의 개수
    P = int(input())
    ans = [] #버스 수

    for i in range(P):
        C = int(input())
        ans.append(bus_count(C))

    print("#{}".format(tc),end=' ')
    print(' '.join(map(str,ans)))