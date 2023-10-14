class Solution:
    def closeStrings(self, s1: str, s2: str) -> bool:
        return set(s1) == set(s2) and Counter(Counter(s1).values()) == Counter(Counter(s2).values())
