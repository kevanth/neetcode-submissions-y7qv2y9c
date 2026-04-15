class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for currStr in strs:
            out+=str(len(currStr))+"😊"+currStr
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        currLen = 0
        currWord = ""
        j = 0
        i = 0
        print(s)
        while i < (len(s)):
            if s[i] == "😊":
                print(s[j:i])
                currLen = int(s[j:i])
                i += 1
                currWord = s[i:i+currLen]
                out.append(currWord)
                j = i+currLen
                i = i+currLen
            i+=1
        return out     