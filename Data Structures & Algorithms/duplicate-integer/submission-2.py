class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        new_set = set()

        # adds each element from nums to new_set checks if each element within the newly created set is a duplicate 
        for num in nums:
            if num in new_set:
                return True
            new_set.add(num)
        return False

        
        