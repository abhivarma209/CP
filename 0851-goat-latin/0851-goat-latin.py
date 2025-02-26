class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        words = sentence.split(" ")
        for i,word in enumerate(words):
            if word[0] in vowels:
                words[i] = word + "ma" + 'a' * (i+1)
            else:
                words[i] = word[1:] + word[0] + "ma" + 'a' * (i+1)
        return " ".join(words)