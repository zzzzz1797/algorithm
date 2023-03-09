"""
    请你判断一个9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

    数字1-9在每一行只能出现一次。
    数字1-9在每一列只能出现一次。
    数字1-9在每一个以粗实线分隔的3x3宫内只能出现一次。（请参考示例图）

    注意：
        一个有效的数独（部分已被填充）不一定是可解的。
        只需要根据以上规则，验证已经填入的数字是否有效即可。
        空白格用'.'表示。

"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_set = set()
        row_set = set()
        box_set = set()

        row = len(board)
        col = len(board[0])

        for row_index in range(row):
            for col_index in range(col):
                point = board[row_index][col_index]
                if point == ".":
                    continue

                box_index = (row_index // 3) * 3 + col_index // 3

                col_flag = f"{col_index}-{point}"
                row_flag = f"{row_index}-{point}"
                box_flag = f"{box_index}-{point}"

                if col_flag in col_set or row_flag in row_set or box_flag in box_set:
                    return False

                col_set.add(col_flag)

                row_set.add(row_flag)

                box_set.add(box_flag)
        return True
