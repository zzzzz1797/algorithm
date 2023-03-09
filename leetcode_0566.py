"""
    在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。

    给你一个由二维数组 mat 表示的m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
    重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。
    如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])

        if row * col != r * c:
            return mat

        res = []
        tmp_res = []
        index = 0

        for i in range(row):
            for j in range(col):
                if index < c:
                    tmp_res.append(mat[i][j])
                    index += 1
                if index >= c:
                    res.append(tmp_res)
                    tmp_res = []
                    index = 0
        return res


if __name__ == '__main__':
    print(Solution().matrixReshape([[1, 2], [3, 4]], 1, 4))
