class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        if target in nums and len(nums) == 1:
            return 0
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1