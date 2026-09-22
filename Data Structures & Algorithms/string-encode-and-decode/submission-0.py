class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s # Puts the length of the string followed by a delimiter then the string
        return result
    def decode(self, s: str) -> List[str]:
        result, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length]) # appends each full word into the result array

            i = j + 1 + length # sets i to the beginning of the next word
        return result
        
