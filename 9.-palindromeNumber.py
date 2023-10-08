class Solution(object):
    def isPalindrome(self, x):
         lista = []
         for i in str(x):
              lista.append(i)
         if lista == lista[::-1]:
               return True
         return False


solution = Solution()
result = solution.isPalindrome

print(result(121))
