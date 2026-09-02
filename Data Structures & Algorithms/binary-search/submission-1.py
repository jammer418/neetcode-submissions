class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while target >= nums[l] and target <= nums[r]:
            midIndex = (l + r) // 2 
            if l == r:
                if nums[l] == target:
                    return l
                else:
                    return -1
            if target == nums[midIndex]:
                return midIndex
            elif target < nums[midIndex]:
                r = midIndex - 1
            else: 
                l = midIndex + 1
        return -1