## DFS

n = int(input())
string = input()
global ans
ans = []

def dfs(s,e, total, string) :
    global ans

    if s>0 :
        if string[s-1]=='+' :
            total+=eval(string[s:e+1])
        elif string[s-1]=='-' :
            total -= eval(string[s:e + 1])
        elif string[s-1]=='*' :
            total *= eval(string[s:e + 1])
    else :
        total+=eval(string[s:e + 1])
    if e>=len(string)-1 :
        ans.append(total)
        return

    dfs(e+2, e+2, total, string)
    dfs(e+2, e+4, total, string)

dfs(0, 0, 0, string)
print(max(ans))
