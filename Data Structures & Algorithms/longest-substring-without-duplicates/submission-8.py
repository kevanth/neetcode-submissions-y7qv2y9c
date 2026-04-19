class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curMax = 0
        mySet = set()
        ret = 0
        #axbxc---
        #i  j
        #if found dupe, move i in loop till found while subtracting length max
        i = 0
        for j in range(len(s)):
            c = s[j]
            if c in mySet:
                for x in range(i,j):
                    c2 = s[x]
                    i += 1
                    if c2 == c:
                        break
                    curMax -= 1
                    mySet.remove(c2)
            else:
                mySet.add(c)
                curMax += 1
                ret = max(curMax, ret)
            print(s[i:j+1], curMax, ret)
        return ret