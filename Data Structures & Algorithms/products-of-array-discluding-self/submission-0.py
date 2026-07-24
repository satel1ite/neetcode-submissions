class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # 1. Считаем префиксы (включая текущий элемент)
        prefix = [1] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i - 1]
            
        # 2. Считаем суффиксы (включая текущий элемент)
        suffix = [1] * n
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1): # Идем до 0 включительно
            # Умножаем текущее число на накопленный суффикс СПРАВА
            suffix[i] = nums[i] * suffix[i + 1] 
            
        # 3. Собираем ответ
        ans = [1] * n
        for i in range(n):
            # Если слева ничего нет (i=0), берем 1. Иначе берем префикс слева.
            left_prod = prefix[i - 1] if i > 0 else 1
            
            # Если справа ничего нет (i=n-1), берем 1. Иначе берем суффикс справа.
            right_prod = suffix[i + 1] if i < n - 1 else 1
            
            ans[i] = left_prod * right_prod
            
        return ans