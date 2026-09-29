class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars) # counts the freq of each character in the given string
        res = 0;

        for w in words:
            cur_words = defaultdict(int) # freq of each character in each word in the words list
            good = True;
            for c in w: # for each character in each word
                cur_words[c] += 1
                if cur_words[c] > count[c]: # if char is found more in the work than the string
                    good = False # does not work
                    break
            if good:
                res += len(w)
        return res