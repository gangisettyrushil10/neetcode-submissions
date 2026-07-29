class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        groups = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for char in str:
                index = ord(char) - ord('a')
                count[index] += 1
            key = tuple(count)
            groups[key].append(str)
        return list(groups.values())