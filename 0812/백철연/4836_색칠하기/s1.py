import sys
sys.stdin = open('sample_input.txt')

TC= int(input())
for tc in range(1, TC+1):
    N = int(input())
    data= [[0]*10 for _ in range(10)]

    cnt = 0


    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        #print(r1,c1,r2,c2,color)
        for i in range(r1,r2+1):
            for j in range(c1, c2+1):
                data[i][j] += color

    for i in range(10):
        for j in range(10):
            if data[i][j] == 3:
                cnt += 1

    print('#{} {}'.format(tc,cnt))















