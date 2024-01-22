class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        
        for i, num in enumerate(nums):
            comp = target - num
            if comp in num_dict:
                return [num_dict[comp], i]
            num_dict[num] = i
        return None 