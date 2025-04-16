class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result=[] 
        people.sort(key=lambda x: (-x[0], x[1]))                
        for a in people:
            result.insert(a[1], a)
        return result  


class Solution:
     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        result = []
        for h, k in sorted(people, key=lambda x: (-x[0], x[1])):
            result.insert(k, [h, k])
        return result