"""
    给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
    请注意，必须在不复制数组的情况下原地对数组进行操作。

    示例 1:
        输入: nums = [0,1,0,3,12]
        输出: [1,3,12,0,0]

    示例 2:
        输入: nums = [0]
        输出: [0]
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

    def answer_1(self, nums):
        move_index = 0

        for index, num in enumerate(nums):
            if num != 0:
                nums[move_index], nums[index] = nums[index], nums[move_index]
                move_index += 1

    def answer_2(self, nums):
        slow_index = 0

        length = len(nums)

        for index, num in enumerate(nums):
            if num != 0:
                nums[slow_index] = num
                slow_index += 1

        for tmp_slow_index in range(slow_index, length):
            nums[tmp_slow_index] = 0
