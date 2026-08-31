class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for i in nums:
            if not frequency.get(i):
                frequency[i] = 1
                continue
            frequency[i] += 1
        sorted_frequency = sorted(frequency, key=frequency.get, reverse=True)
        return sorted_frequency[:k]
