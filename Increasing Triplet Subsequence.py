class Solution:
    def increasingTriplet(self, nums):
        f = float('inf')
        s = float('inf')
        
        for n in nums:
          
            if n <= f:
                f = n
            elif n <= s:
                s = n
            elif n > s:
                return True
                return False
