class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count =0
        for s in patterns:
            if word.find(s) != -1:
                count +=1
        return count