class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        f = len(words)
        for word in words:
            for char in word:
                if char not in allowed:
                    f -= 1
                    break
        return f
                    
            
            
