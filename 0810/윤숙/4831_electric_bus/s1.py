import sys
sys.stdin=open('input.txt')
T=int(input())
for tc in range(1,T+1):
    #K-> 한번 충전으로 최대한 이동할 수있는 정류장 수
    #N-> 종점
    #M-> 충전기가 설치된 정류장번호 갯수
    #M_n -> 충전기가 설치된 정류장번호
    #출력 노선번호 출력 횟구
    K,N,M=map(int,input().split())
    M_n=list(map(int,input().split()))
    charger_count=0
    Bus_Station=[0]*(N+1)
    Bus_charger=[0]*(N+1)
    Bus_Station[N]=1

    for idx in range(0,len(Bus_Station),K):
        Bus_Station[idx]+=1
        Bus_charger[0]=1

    for idx in M_n:
        Bus_charger[idx]+=1

    Station_idx=0

    for i in range(station_idx,N,K):

        if Bus_Station[i]==1 & Bus_charger[i]==1:
            charger_count+=1
            station_idx=i


        elif Bus_Station[i]==1 & Bus_charger[i]==0:
            for j in range(i,0,-1):
                if Bus_charger[j] == 1:
                    charger_count += 1
                    break
                else

        elif Bus_Station[i]==0 & Bus_charger[i]==1



    print(Bus_Station)
    print(Bus_charger)
    print(charger_count)