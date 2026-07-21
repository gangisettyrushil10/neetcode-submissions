class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s != len_t: 
            return False

        count_s = {}
        count_t = {}

        for char in s: 
            count_s[char] = count_s.get(char, 0) + 1

        for char in t: 
            count_t[char] = count_t.get(char, 0) + 1

        if count_t == count_s: 
            return True
        else: 
            return False