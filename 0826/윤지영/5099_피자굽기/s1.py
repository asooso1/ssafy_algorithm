import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    pizza = list(map(int,input().split())) # 피자번호 순서대로의 치즈 양
    q = [] * N                              # 화덕 queue 생성
    front = 0                              # queue 초기화
    cnt = list(range(1,N+1))              # 화덕 내부 피자 번호
    for _ in range(N):
        q.append(pizza.pop(0))           # 화덕 최대치만큼 피자 넣기

    while len(q) > 1:
        if q[front] != 0:               # 화덕 내부 1번째 치즈양이 0이 아니면
            q[front] //= 2              # //2 만큼 감소
            if q[front] == 0:           # 화덕 내부 1번째 치즈양이 0 이면
                q.pop(front)            # 화덕 내부에서 해당 피자 꺼내기
                if pizza:               # 아직 넣을 피자가 남았다면
                    q.insert(front,pizza.pop(0))    # 남은 피자 중 첫번째 피자를, 빼낸 자리에 넣기
                    N += 1                      # 처음에 화덕에 N번까지 넣었으니까, 새로 넣을 피자는 N+1번 -> N+2번 ...
                    cnt[front] = N              # 화덕 내부 피자 번호 갱신
                else:                   # 넣을 피자가 없다면
                    cnt.pop(front)      # 치즈 양이 0이 된 피자를 꺼내고 새로 넣는게 없으므로 화덕 내부 피자 번호도 같이 없애기
                    front %= len(q)     # 인덱스 에러 방지
            else:
                front = (front + 1) % len(q)        # front 갱신(화덕 내부에서 돌아야하므로 q 길이로 나눈 나머지로 갱신)
    print('#{} {}'.format(tc, cnt[0]))



# q = [[1,7],[2,2],[3,6]] 처럼 인덱스랑 같이 넣는 방법으로도 해볼 것것






