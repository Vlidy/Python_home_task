class Solution(object):
    def removeOuterParentheses(self, s):
        result=""
        postr="("
        counter=1
        for x in range(1,len(s)):
            if s[x]=="(":
                counter+=1
                postr+="("
            else:
                counter-=1
                postr+=")"
            if counter==0:
                result+=postr[1:-1]
                postr=""
        return result

        
            
        
        