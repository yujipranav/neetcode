class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        l, r = 0, n - 1
        
        # this while loop is to find the pivot in nums
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m


        pivot = l
        l, r = 0, n - 1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot #it means the target is on the right of the pivot

        else:
            r = pivot - 1 #it means the target is on the left of the pivot

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1

            else:
                r = m - 1

        return -1
        