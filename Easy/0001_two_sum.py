# Problem: Two Sum
# Difficulty: Easy

class Solution(object):
  def twoSum(self, nums, target):
    for index_i,i in enumerate(nums):
      for index_j,j in enumerate(nums[1:], start=1):
        if i + j == target:
          return [index_i, index_j]