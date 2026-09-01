class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        for num in nums:
            if not group.get(num):
                group[num] = 1
                continue
            group[num] += 1
        groups_ordered = sorted(group, key=group.get, reverse=True)
        return groups_ordered[:k]
