class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.index(needle) if haystack.count(needle) > 0 else -1
solution = Solution()
result = solution.strStr

print(result("sadbutsad", "sad"))
