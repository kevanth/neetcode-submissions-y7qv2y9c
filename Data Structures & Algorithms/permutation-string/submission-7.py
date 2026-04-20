class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(0,len(s2)):
            c = s2[i]
            #if match:
            if c in s1:
                remainingToMatch = s1
                for j in range(i, i+len(remainingToMatch)):
                    if j>=len(s2):
                        break
                    if s2[j] in remainingToMatch:
                        remainingToMatch = remainingToMatch.replace(s2[j], "",1)
                    else:
                        break
                    if len(remainingToMatch) == 0:
                        return True
        return False
