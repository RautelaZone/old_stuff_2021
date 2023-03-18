class Solution:
    def hayNeed(self, haystack: str, needle: str) -> int:
        print("Index of the first occurrence of needle in haystack is:")
        if len(haystack) <= 0 and len(needle) > 0:
            raise Exception('Empty Haystack')
        elif len(needle) <= 0 and len(haystack) > 0:
            raise Exception('Empty Needle')
        elif len(haystack) == 0 and len(needle) == 0:
            return 0
        else:
            for i in range(len(haystack)):
                if haystack[i:i + len(needle)] == needle:
                    return i
            return -1


haystack = "hello"
needle = "ll"
s = Solution()
print(s.hayNeed(haystack, needle))
