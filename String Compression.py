class Solution:
    def compress(self, chars: List[str]) -> int:
        n=len(chars)
        left,right,k=0,0,0
        while left<n:
            left=right
            while right<n and chars[right]==chars[left]:
                right+=1
            chars[k]=chars[left]
            k+=1
            if (right-left)>1:
                for l in str(right-left):
                    chars[k]=l
                    k+=1
            left=right
        return k
