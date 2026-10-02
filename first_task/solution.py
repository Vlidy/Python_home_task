class Solution(object):
    def isToeplitzMatrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        # mass=[]
        # for x in range(0,n):
        #     s=""
        #     for y in range(m):
        #         s+=str(matrix[x][y])
        #     mass.append(s)
        if n==1 or m==1:
            return True
        else:
            for x in range(n-1):
                if matrix[x][:-1]!=matrix[x+1][1::]:
                    return False
            return True