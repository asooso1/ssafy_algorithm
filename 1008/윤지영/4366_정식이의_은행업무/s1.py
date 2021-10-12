import sys
sys.stdin = open('sample_input (1).txt')

# 2진수 계산
def cal_binary(n):
    ans = 0
    li = n[::-1]
    for i in range(len(n)):
        ans += (2**i) * li[i]
    return ans

# 3진수 계산
def cal_trit(n):
    ans = 0
    li = n[::-1]
    for i in range(len(n)):
        ans += (3**i) * li[i]
    return ans


T = int(input())
for tc in range(1,T+1):
    binary = list(map(int,input()))
    trit = list(map(int,input()))
    i = j = 0

    # 가능한 경우의 수를 모두 담을 리스트 reb,ret
    reb = [0] * len(binary)
    ret = [0] * (2*len(trit))

    # 무조건 1자리가 틀리다고 하였으므로 2진수에서 틀린 자릿수 i
    while i < len(binary):
        # 원래 값을 temp에 저장해두고, 바꾼 후 계산하여 reb 리스트에 담고, 다시 원래 값 복구 -> 다음 자리수 변경 반복
        temp = binary[i]
        binary[i] = (binary[i]+1) % 2
        reb[i] = cal_binary(binary)
        binary[i] = temp
        i += 1

    # 3진수는 1,2,3에서 바뀌므로 한 자리에서 바뀔 수 있는 경우가 2가지 존재
    # -> 자릿수 인덱스와 ret 배열에 넣을 인덱스에서 차이가 생겨서, 배열에 넣을 인덱스는 새로운 인덱스 m 사용
    m = 0

    # 3진수에서 틀린 자릿수 j
    while j < len(trit):
        temp2 = trit[j]
        for k in range(1,3):
            trit[j] = (trit[j]+1) % 3
            ret[m] = cal_trit(trit)
            m += 1
        # 해당 자릿수에서 바꿀 수 있는 경우를 반복문을 통해 모두 배열에 넣고, 다시 원래값 복구 후 다음 자릿수 변경 반복
        trit[j] = temp2
        j += 1
    result = 0

    # 가능한 수를 모두 배열에 담았으므로, 배열을 순회하며 같은 값이 존재하면 result에 담고 break
    for i in range(len(ret)):
        for j in range(len(reb)):
            if ret[i] == reb[j]:
                result = ret[i]
                break
        if result:
            break
    print('#{} {}'.format(tc,result))






# def check(n,m, li2,li3):
#     global b,t, reb, ret
#     if n >= len(li2) or m >= len(li3):
#         return False
#     if b == t :
#         reb,ret = li2,li3
#         return True
#
#     else:
#         temp = li2[i]
#         li2[i] = (li2[i] + 1) % 2
#         b = cal_binary(li2)
#
#         temp2 = li3[j]
#         for k in range(1,3):
#             li3[j] = (li3[j] + k) % 3
#             t = cal_trit(li3)
#             if check(i+1,j+1,li2,li3):
#                 return
#             li3[j] = temp2
#             li2[i] = temp

