class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        solution = []
        result = []
        n = len(nums)
        def backtrack(i):
            if i == n:
                result.append(solution[:])
                return
            #Ignora o numero
            backtrack(i+1)
            
            # Não ignora
            solution.append(nums[i])
            backtrack(i+1)
            solution.pop()
            
        backtrack(0)
        return result



        