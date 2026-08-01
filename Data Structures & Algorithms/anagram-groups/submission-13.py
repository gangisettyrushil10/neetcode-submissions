class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        groups = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for char in str: 
                count[ord(char) - ord('a')] += 1
            groups[tuple(count)].append(str)

        return list(groups.values())
  