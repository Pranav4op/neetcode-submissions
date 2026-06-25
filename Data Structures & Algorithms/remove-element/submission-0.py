class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = k = 0
        a = nums
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
                k+=1

        print(nums)
        return k