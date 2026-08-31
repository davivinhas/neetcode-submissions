class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in group_dict:
                group_dict[key] = []
            group_dict[key].append(str)
        return list(group_dict.values())
        