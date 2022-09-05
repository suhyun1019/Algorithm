n=int(input())
k=0   # 수열의 index

def s_len(k) :   # 수열 s의 길이 구하는 함수
    if k==0:
        return 3
    return 2*s_len(k-1)+(k+3)

def answer(s,n,k):   # s는 수열의 길이, n은 원하는 n번째 알파벳, k는 수열의 인덱스
    h=(s-k-3)/2   # s(k)에서 s(k-1)의 길이
    if s==3:   # 수열 s의 길이가 3일때 (가장 작은 사건), s(0)=moo
        if n==1:
            return "m"
        else:
            return "o"
    else:
        if h<n and n<=h+k+3:   # n이 o가 k+2인 수열에 있을 때
            if n==h+1:
                return "m"
            else:
                return "o"
        elif n<=h:   # n이 중간보다 작을 때
            return answer(s_len(k-1),n,k-1)
        else:   # n이 중간보다 클 때
            return answer(s_len(k-1),n-h-(k+3),k-1)


while (n>=s_len(k)):   # 수열 길이가 n보다 클 때까지 k증가
    k+=1
s=s_len(k)   # n을 포함하는 최소 길이의 수열

print(answer(s,n,k))