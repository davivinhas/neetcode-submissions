class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_num = dict()
        for i in nums:
            if count_num.get(i):
                return True
            count_num[i] = 1
        return False