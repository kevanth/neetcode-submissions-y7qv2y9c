class Solution:
    def isPalindrome(self, s: str) -> bool:
        #odd
        s = ''.join(c.lower() for c in s if c.isalnum())
        if len(s)%2 != 0:
            #remove mid
            s = s[:len(s)//2] + s[len(s)//2+1:]
        #even
        print(s)
        rev = ""
        for i in range((len(s)//2)-1,-1,-1):
            rev += s[i]
        if rev == s[len(s)//2:]:
            return True
        return False