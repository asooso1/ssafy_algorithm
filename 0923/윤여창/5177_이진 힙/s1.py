import sys
sys.studin = open('sample_input.txt')

def change(i):                   # 노드 값 비교하면서 계속 바꿔주는
    if i != 0:
        if nd[i//2] > nd[i]:
            nd[i], nd[i//2] = nd[i//2], nd[i]
            change(i//2)

def sum_hp(N):                   # 정렬된 노드 값에서 조상노드값들 더하기 함수
    total_sum = 0
    while N:
        N //= 2
        total_sum += nd[N]
    return total_sum

T = int(input())                        #기본 셋팅
for tc in range(1, T + 1):
    N = int(input())
    nd = [0] + list(map(int, input().split()))
    for i in range(1, len(nd)):
        change(i)

    print('#{} {}'.format(tc, sum_hp(N)))