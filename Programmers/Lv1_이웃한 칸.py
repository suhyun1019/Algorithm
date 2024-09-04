def solution(board, h, w):
    answer = 0
    move = [(1,0), (0,1), (-1,0), (0,-1)]
    
    for i in range(4) :
        dh, dw = h+move[i][0], w+move[i][1]
        if 0<=dh<len(board) and 0<=dw<len(board) and board[h][w]==board[dh][dw] :
            answer+=1
    return answer
