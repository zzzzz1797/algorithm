"""
    给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。在「杨辉三角」中，每个数是它左上方和右上方的数的和。

    示例 1:
        输入: numRows = 5
        输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    示例2:
        输入: numRows = 1
        输出: [[1]]

"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for index in range(numRows):
            row = [0] * (index + 1)
            row[0] = 1
            row[-1] = 1

            for j in range(1, index):
                row[j] = res[index - 1][j] + res[index - 1][j - 1]
            res.append(row)

        return res
