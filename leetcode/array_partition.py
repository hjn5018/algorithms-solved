class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
# https://leetcode.com/problems/array-partition/submissions/1472616614/
