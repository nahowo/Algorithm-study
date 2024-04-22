class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = -1
        hl = len(haystack)
        nl = len(needle)
        for i in range(hl - nl + 1):
            if haystack[i] == needle[0]:
                if haystack[i : i + nl] == needle:
                    idx = i
                    return idx
        return idx
