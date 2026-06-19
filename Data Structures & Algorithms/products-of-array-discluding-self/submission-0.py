class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1] * len(nums)
        p[0] = nums[0]
        s = [1] * len(nums)
        res = []
        s[len(nums) - 1] = nums[len(nums) - 1]
        res = []
        for i in range(1, len(nums)):
            p[i] = p[i - 1] * nums[i]
        for i in range(len(nums) - 2, -1, -1):
            s[i] = s[i + 1] * nums[i]

        for i in range(0, len(nums)):
            if i == 0:
                res.append(s[i + 1])
            elif i == len(nums) - 1:
                res.append(p[i - 1])
            else:
                res.append(p[i - 1] * s[i + 1])
        return res
