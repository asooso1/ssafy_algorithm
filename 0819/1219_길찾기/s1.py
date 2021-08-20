import sys
<<<<<<< HEAD
sys.stdin = open("input.txt")

for _ in range(1, 11):
    tc, road = map(int,input().split())
    maps = list(map(int,input().split()))
    nmaps = []
    ans = 0
    stack = []
    already = []
    for i in range(road):
        nmaps.append([maps[2*i],maps[2*i+1]])

    s = 0
    while True:
        if s == 99:
            ans = 1
            break

        for i in range(road):
            if nmaps[i][0] == s and nmaps[i] not in stack and nmaps[i] not in already:
                stack.append(nmaps[i])
                s = nmaps[i][1]
                break

        else:
            if stack:
                end = stack.pop()
                s = end[0]
                already.append(end)
            else:
                break

    print("#{} {}".format(tc,ans))
=======
sys.stdin = open('input.txt')

def DFS():
    visted = [0] * 100
    stack = []
    visted[0] = 1  # 처음은 무조건 방문

    while stack:
        if stack[-1] == 99:  # 마지막 방문한 곳이 도착점이라면 1
            return 1

        # 방문하고, pop
        v = stack[-1]
        visted[v] = 1
        stack.pop()

        if adjacency.get(v, -1).get(v, -1) != -1:
            for i in adjacency[v]:
                if visted[i] == 0:
                    stack.append(i)

        if visted[99]:
            return 1
        else:
            return 0


for _ in range(1):
    test_case, roads = map(int, input().split())
    pair_list = list(map(int, input().split()))

    adjacency = dict()  # 인접정보를 저장하는 dict
    for i in range(0, roads*2, 2):  # 99까지 받을 순 없으니 각 노드 별 경로를 저장하는 방식
        if adjacency.get(pair_list[i], -1) == -1:
            adjacency[pair_list[i]] = [pair_list[i+1]]
        else:  # key가 있으면 key 옆의 value append
            adjacency[pair_list[i]].append(pair_list[i+1])


    print('#{} {}'.format(test_case, DFS()))


>>>>>>> 92ff47ec2ac89df817400374cabd441bfa841964
