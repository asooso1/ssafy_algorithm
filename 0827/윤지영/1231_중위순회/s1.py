import sys
sys.stdin = open("input.txt")

def inorder(n):
    if n:
        inorder(adjList[n][0])      # 왼쪽
        result.append(G[n])
        inorder(adjList[n][1])      # 오른쪽

for tc in range(1,11):
    N = int(input())    # 정점의 수
    nums = [input().split() for _ in range(N)]
    for k in range(N):
        nums[k].append(0)
        nums[k].append(0)
    G = [0] + [nums[i][1] for i in range(N)]
    adjList = [[0,0] for _ in range(N+1)]
    for j in range(N):
        p = int(nums[j][0])
        if adjList[p][0] == 0:
            if nums[j][2] != 0:
                c_l = int(nums[j][2])
                adjList[p][0] = c_l
        if adjList[p][0] and nums[j][3] != 0:
            c_r = int(nums[j][3])
            adjList[p][1] = c_r
    result = []
    inorder(1)
    print('#{} {}'.format(tc, ''.join(map(str,result))))