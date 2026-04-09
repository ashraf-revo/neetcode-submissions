class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        leftI=0
        rightI=0
        result=""
    
        while leftI+rightI<len(word1)+len(word2):

            if leftI<len(word1):
                result +=word1[leftI]
                leftI +=1

            if rightI<len(word2):
                result +=word2[rightI]
                rightI +=1

        return result    