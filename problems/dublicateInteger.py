# find the duplaicate input, if in list of integer has dupilcacy return true else return false

class Solution:
    def duplicate(self, nums: list[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

solution = Solution()
nums = [1,2,3,4,1]
print(solution.duplicate(nums))