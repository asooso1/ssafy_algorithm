import sys
sys.stdin = open('input.txt')

def emu(n):
    li = node[:]
    if li[n] == '/':
        li[n] = float(li[left[n]]) / float(li[right[n]])
    elif node[n] == '*':
        li[n] = float(li[left[n]]) * float(li[right[n]])
    elif node[n] == '+':
        li[n] = float(li[left[n]]) + float(li[right[n]])
    elif node[n] == '-':
        li[n] = float(li[left[n]]) - float(li[right[n]])
    return li

for tc in range(1,11):
    N = int(input())
    node = [0] * (N+1)
    left = [0] * (N+2)
    right = [0] * (N+2)
    for _ in range(N):
        input_li = input().split()
        idx = int(input_li[0])
        if input_li[1].isdigit():
            node[idx] = int(input_li[1])
        else:
            node[idx] = input_li[1]
            left[idx] = int(input_li[2])
            right[idx] = int(input_li[3])
    for m in range(N,0,-1):
        if type(node[m]) == str:
            node = emu(m)

    print('#{} {}'.format(tc, int(node[1])))
    

        
# 자식노드가 항상 *2, *2+1 형태가 아니여서 틀린 답
# def emu(n):
#     if node[n] == '/':
#         node[n] = float(node[n*2]) / float(node[n*2+1])
#     elif node[n] == '*':
#         node[n] = float(node[n*2]) * float(node[n*2+1])
#     elif node[n] == '+':
#         node[n] = float(node[n*2]) + float(node[n*2+1])
#     elif node[n] == '-':
#         node[n] = float(node[n*2]) - float(node[n*2+1])


# for tc in range(1,11):
#     N = int(input())
#     node = [0] * (N+1)
#     left = [0] * (N+1)
#     right = [0] * (N+1)
#     for _ in range(N):
#         input_li = input().split()
#         idx = int(input_li[0])
#         if input_li[1].isdigit():
#             cnt = int(input_li[1])
#         else:
#             cnt = input_li[1]
#         node[idx] = cnt
#         if idx == 1:
#             left[idx] = cnt
#         else:
#             if idx % 2 :
#                 right[idx] = cnt
#             else:
#                 left[idx] = cnt
#     for m in range(N//2,0,-1):
#         if type(node[m]) == str:
#             if (m*2 <= N) and (m*2+1 <=N):
#                 emu(m)
#     print(int(node[1]))
