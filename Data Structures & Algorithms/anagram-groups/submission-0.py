class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = {}

        for word in strs:
            
            sort_word = "".join(sorted(word))
            
            if sort_word not in anagram_map:
                anagram_map[sort_word] = []

            anagram_map[sort_word].append(word)

        return list(anagram_map.values())
