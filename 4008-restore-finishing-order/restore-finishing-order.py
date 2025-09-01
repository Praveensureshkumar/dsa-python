class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result=[]
        for i in order:
            if i in friends:
                result.append(i)
        return result

        