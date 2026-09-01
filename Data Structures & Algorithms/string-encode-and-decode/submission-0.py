class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + ":" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        colonIndex = s.find(":")
        wordLength = int(s[0:colonIndex])
        word = s[colonIndex + 1:colonIndex + 1 + wordLength]
        return [word] + self.decode(s[colonIndex + 1 + wordLength:])