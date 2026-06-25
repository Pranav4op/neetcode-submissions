class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [1] * len(arr)
        ans[len(arr)-1]=-1
        rightmax = -1
        for i in range(len(arr)-2,-1,-1):
            if arr[i+1]>rightmax:
                rightmax = arr[i+1]
            ans[i] = rightmax
        return ans