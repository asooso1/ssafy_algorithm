import sys
sys.stdin = open('input.txt')

test_case = int(input())
for test in range(test_case):

    x = [-1, 0, 1]
    y = [0, -1, 0]    # 좌-상-우

    ladder_arr = []
    for _ in range(100):
        ladder_arr.append(list(map(int, input().split())))

    pt_dy = 98
    pt_dx = ladder_arr[99].index(2)  # type: int


    # # 위로 갈 때 좌우 탐색 후 좌우 방향 전환
    # def Up_Left_Right(a, b):
    #     if ladder_arr[b][a-1] == 1:
    #         return Left_Up(a-1, b)
    #     elif ladder_arr[b][a+1] == 1:
    #         return Right_up(a+1,b)
    #     else:
    #         return Up_Left_Right(a, b-1)
    #
    # # 왼쪽으로 갈 때 위 탐색 후 방향 전환
    # def Left_up(a, b):
    #     if ladder_arr[b-1][a] ==1:
    #         return Up_Left_Right(a,b-1)
    #     else:
    #         return Left_up(a-1, b)
    #
    # # 오른쪽으로 갈 때 위 탐색 후 방향 전환
    # def Right_up(a, b):
    #     if ladder_arr[b-1][a] == 1:
    #         return Up_Left_Right(a, b-1)
    #     else:
    #         return Right_up(a+1, b)
    #
    # Up_Left_Right(pt_dx, pt_dy)


    # while pnt_dy >0:
    #     if ladder_arr[pnt_dy][pnt_dx-1] == 1:
    #         while ladder_arr[pnt_dy][pnt_dx-1] == 1:
    #             if pnt_dx == 0:
    #                 break
    #             else:
    #                 pnt_dx -= 1
    #     elif ladder_arr[pnt_dy][pnt_dx+1] == 1:
    #         while ladder_arr[pnt_dy][pnt_dx+1] == 1:
    #             pnt_dx += 1
    #             if pnt_dx == 99:
    #                 break
    #     else:
    #         pnt_dy -= 1
    #
    # print(pnt_dx)