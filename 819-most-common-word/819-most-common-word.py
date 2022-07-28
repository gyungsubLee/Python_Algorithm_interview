import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words =[word for word in re.sub('[^\w]',' ', paragraph).lower().split() if word not in banned]
        Fre = collections.defaultdict(int)
        for word in words:
            Fre[word] += 1
            
        return max(Fre, key=Fre.get)