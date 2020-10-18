class Solution(object):
    def search(self, nums, target):

        if nums is None or len(nums) == 0:
            return False

        nums = list(set(nums))
        start = 0
        end = len(nums) - 1
        rightMost = nums[-1]

        while start <= end:
            mid = int((start + end) / 2)

            if nums[mid] == target:
                return True

            if nums[mid] > rightMost:
                if target < nums[mid] and target > rightMost:  # we know everything before mid is also > rightMost
                    end = mid - 1

                else:  # target is more than rightMost
                    start = mid + 1

            else:  # we know rotation happened to the left
                if target > nums[
                    mid] and target <= rightMost:  # you know to right is increasing so go there if targ > mid
                    start = mid + 1

                else:
                    end = mid - 1

        return False