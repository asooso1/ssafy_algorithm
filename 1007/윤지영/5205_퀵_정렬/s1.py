import sys
sys.stdin = open('sample_input (1).txt')

def quick(l,L,R):
    if L < R:
        s = partition(l,L,R)
        quick(l,L,s-1)
        quick(l,s+1,R)

def partition(l,L,R):
    # 피봇값을 제일 왼쪽값으로 설정
    p = l[L]
    i,j = L,R
    while i <= j :
        while i <= j and l[i] <= p:
            i += 1
        while i <= j and l[j] >= p :
            j -= 1
        if i <= j :
            l[i], l[j] = l[j], l[i]
    l[L], l[j] = l[j], l[L]
    return j

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    quick(lst, 0, N-1)
    print('#{} {}'.format(tc,lst[N//2]))
