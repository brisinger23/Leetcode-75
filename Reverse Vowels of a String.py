class Solution:
    def reverseVowels(self, word: str) -> str:
        start=0
        end=len(word)-1
        vowels= ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
        s=[word[i] for i in range(len(word))]
        while start<end:
            if s[start] in vowels:
                while start<end and s[end] not in vowels:
                    end-=1
                aux=s[start]
                s[start]=s[end]
                s[end]=aux
                end-=1
            start+=1
        res=""
        for i in s:
            res+=i
        return res
