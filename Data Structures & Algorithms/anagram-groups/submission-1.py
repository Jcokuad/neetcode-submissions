class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = {} #Creates a new array for the output

        for word in strs: #Runs through each word un the strs array
            
            sort_word = "".join(sorted(word)) #Sorts each word to get letters used in each word
            
            if sort_word not in anagram_map:
                anagram_map[sort_word] = [] # Creates new list if new letter combination found

            anagram_map[sort_word].append(word) # Puts the word in its list

        return list(anagram_map.values()) # Returns an array of the sorted values.
