class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4, -1, -1, 0, 1, 2]
        sorted_nums = sorted(nums) # O(nlogn)
        result = []
        for i in range(len(nums)):
            if i > 0 and sorted_nums[i - 1] == sorted_nums[i]:
                continue
            left = i + 1
            right = len(nums) - 1
            target = 0 - sorted_nums[i]
            while left < right:
                if sorted_nums[left] + sorted_nums[right] < target:
                    left += 1
                elif sorted_nums[left] + sorted_nums[right] > target:
                    right -= 1
                else:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right + 1]:
                        right -= 1
        return result
        