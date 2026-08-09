class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common = Counter(words[0])

        for word in words[1:]:
            common=Counter(common)&Counter(word)


        res=[]
        for key,value in common.items():
            for i in range (value):
                res.append(key)

        return res
           
       
        