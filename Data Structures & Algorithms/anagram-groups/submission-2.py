class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # groups = defaultdict(list)

        # for str in strs:
        #     key = tuple(sorted(str))
        #     groups[key].append(str)

        # return list(groups.values())

        groups = defaultdict(list)

        for str in strs:
            count = [0] * 26
            for char in str: 
                index = ord(char) - ord('a')
                count[index] += 1

            groups[tuple(count)].append(str)


        return list(groups.values())
