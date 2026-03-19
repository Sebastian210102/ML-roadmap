def isAnagram(self, s: str, t: str) -> bool:
        dict_anagram = {
        }
        if len(s) != len(t):
            return False

        for letter in s:
            dict_anagram[letter] = dict_anagram.get(letter, 0) + 1

        for letter in t:
            if letter not in dict_anagram or dict_anagram[letter] == 0:
                return False
            dict_anagram[letter] = dict_anagram.get(letter)-1
        
        return True