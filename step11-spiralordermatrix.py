def spiralordermatrix(self,matrix):
    result=[]
    if not matrix:
        return result
    top,bottom=0,len(matrix)-1
    left,right=0,len(matrix[0])-1
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
            
