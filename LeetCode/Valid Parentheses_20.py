class Solution:
    def isValid(self, s: str) -> bool:
        dic={")":"(", "}":"{", "]":"["}
        stack=[]
        
        for i in s :
            if i=="(" or i=="{" or i=="[" :
                stack.append(i)
            elif i==")" or i=="}" or i=="]" :
                if len(stack)==0 :
                    return False
                elif stack[-1]!=dic[i] :
                    return False
                else :
                    stack.pop()
    
        if len(stack)==0 :
            return True
        else :
            return False
