class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1] * len(nums)
        resL = 1
        resR = 1
        res = []
        for i in range(len(nums) - 1):
            resL *= nums[i]
            left.append(resL)
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
            right.append(resR)
        for i in range(len(nums)):
            res.append(left[i] * right[i]) 
        return res

        