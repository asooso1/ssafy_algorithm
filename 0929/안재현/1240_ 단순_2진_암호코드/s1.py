import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

print(arr)