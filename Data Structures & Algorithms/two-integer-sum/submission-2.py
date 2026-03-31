class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            if nums[i] not in nums_map:
                remain = target-nums[i]
                nums_map[remain] = i
            else:
                return [nums_map[nums[i]], i]

        
        