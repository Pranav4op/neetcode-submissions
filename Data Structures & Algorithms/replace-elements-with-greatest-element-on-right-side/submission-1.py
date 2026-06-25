class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [1] * len(arr)
        ans[len(arr)-1]=-1
        rightmax = -1
        for i in range(len(arr)-2,-1,-1):
            rightmax = max(rightmax,arr[i+1])
            ans[i] = rightmax
        return ans