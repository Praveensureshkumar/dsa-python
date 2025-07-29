class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        top=0
        button=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        while top<=button and left<=right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1
            for i in range(top,button+1):
                result.append(matrix[i][right])
            right-=1
            if top<=button:
                for i in range(right,left-1,-1):
                    result.append(matrix[button][i])
            button-=1
            if left<=right:
                 for i in range(button,top-1,-1):
                    result.append(matrix[i][left])
            left+=1
        return result