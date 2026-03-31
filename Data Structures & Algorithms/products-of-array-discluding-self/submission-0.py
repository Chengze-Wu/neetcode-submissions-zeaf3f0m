class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        resL = 1
        resR = 1
        res = []
        for i in range(len(nums) - 1):
            resL *= nums[i]
            left.append(resL)
        for i in range(len(nums) - 1, 0, -1):
            resR *= nums[i]
            right.append(resR)
        for i in range(len(nums)):
            res.append(left[i] * right[len(nums) - i - 1]) 
        return res

        