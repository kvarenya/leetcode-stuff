class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        char_list = []

        for char_s in s:
            char_list.append(char_s)

        for char_t in t:
            if char_t in char_list:
                char_list.remove(char_t)
            else:
                return False

        return True
        