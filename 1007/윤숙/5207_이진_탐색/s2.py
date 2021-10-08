import sys

sys.stdin = open('input.txt')
# 윤지영 (최종)
def search(target,left,right):
    global result, check
    if left > right :
        result = False
        return
    else:
        m = (left + right) // 2
        if A[m] == target:
            return
# True, False 나 +1, -1 같은 식으로 계속 스왑되는 형식으로 구간 연속 선택을 체크하려면,
# 처음 시작을 어디서 하느냐에 따라 분기가 달라지므로 많이 복잡해진다.
# 그러므로 한쪽을 선택하면 하나의 값으로 고정한 후, 다음에 선택했을 때 해당 값이 아니면 선택하는 식으로 체크
        if A[m] < target:
            if check != 1:
                check = 1
                search(target,m+1,right)
            else:
                result = False
                return

        elif A[m] > target:
            if check != -1:
                check = -1
                search(target,left,m-1)
            else:
                result = False
                return

T = int(input())
for tc in range(1,T+1):
    N,M= map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = list(map(int,input().split()))
    cnt = 0
    for i in range(M):
        check = 0
        result = True
        search(B[i], 0, N - 1)
        if result is True:
            cnt += 1
    print('#{} {}'.format(tc,cnt))