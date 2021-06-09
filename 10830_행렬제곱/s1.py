import sys
sys.stdin = open('input.txt')

# 두 행렬의 곱을 구하는 함수
def multiply(matrix_1, matrix_2):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
            result[i][j] %= 1000
    return result

def devide(B, matrix):
    if B == 1:
        return matrix
    elif B == 2:
        return multiply(matrix, matrix)
    else:
        tmp = devide(B//2, matrix)
        if B % 2 == 0: # B가 짝수면
            return multiply(tmp, tmp)
        else: # B가 홀수면
            return multiply(multiply(tmp, tmp), matrix)


N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
answer = devide(B, A)
for i in range(N):
    for j in range(N):
        print(answer[i][j]%1000, end=" ")
    print()