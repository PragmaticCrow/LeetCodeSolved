#optimized <3
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
solution = Solution() 
result = solution.twoSum([10,12,13,12,2,0,1], 1) 

print(result)





# NOT OPTIMAL >:v
#  / 
# V

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         n = -1
#         for i in nums:
#             n += 1
            
#         indice1 = 0
#         indice2 = 0
        
        
#         while nums[indice1] + nums[indice2] == target or nums[indice1] + nums[indice2] != target:
#                 if indice1 == indice2:
#                     indice2 += 1
#                 if nums[indice1] + nums[indice2] != target:
#                      indice2 += 1
#                 elif nums[indice1] + nums[indice2] == target:
#                     return[indice1, indice2] 
#                     break
#                 if indice2 > n:
#                     indice2 = indice2 - indice2 + indice1 + 1
#                     indice1 += 1
# solucion = Solution() 
# resultado = solucion.twoSum([10,12,13,12,2,0,1], 1) 
# print(resultado)


