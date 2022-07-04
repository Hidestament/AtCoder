"""
E - Rotate and Flip
https://atcoder.jp/contests/abc189/tasks/abc189_e
参考: https://imagingsolution.net/imaging/affine-transformation/
参考: https://nullkara.jp/2021/01/24/sankakiabc189/#toc6
"""

import numpy as np
import sys

input = sys.stdin.readline


def main():
    N = int(input())
    coma = []
    for _ in range(N):
        x, y = map(int, input().split())
        coma.append(np.array([[x], [y], [1]]))

    M = int(input())
    operations = [list(map(int, input().split())) for _ in range(M)]

    op1 = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
    op2 = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    op3 = lambda p: np.array([[-1, 0, 2 * p], [0, 1, 0], [0, 0, 1]])
    op4 = lambda p: np.array([[1, 0, 0], [0, -1, 2 * p], [0, 0, 1]])

    op_matrix = [None] * (M + 1)
    op_matrix[0] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    for i in range(1, M + 1):
        if operations[i - 1][0] == 1:
            op_matrix[i] = op1 @ op_matrix[i - 1]
        elif operations[i - 1][0] == 2:
            op_matrix[i] = op2 @ op_matrix[i - 1]
        elif operations[i - 1][0] == 3:
            op_matrix[i] = op3(operations[i - 1][1]) @ op_matrix[i - 1]
        else:
            op_matrix[i] = op4(operations[i - 1][1]) @ op_matrix[i - 1]

    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().split())
        point = op_matrix[a] @ coma[b - 1]
        print(point[0, 0], point[1, 0])


if __name__ == "__main__":
    main()
