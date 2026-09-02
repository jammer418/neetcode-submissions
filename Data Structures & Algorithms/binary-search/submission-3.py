class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left and right pointer to keep track of the edges of the array
        l = 0 
        r = len(nums) - 1
        # as long as the target value is greater, less than, or equal to the first and last value in the array
        while target >= nums[l] and target <= nums[r]:
            midIndex = (l + r) // 2 
            # checks if pointers have converged, if so checks that the value of the middle index is equal to the target and returns middle index. pointers are adjusted appropiately if the target is less than or greater than the value located at middle index
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