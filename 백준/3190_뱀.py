n,k = int(input()), int(input())
apple = [list(map(int, input().split())) for _ in range(k)]
apple = [[apple[i][0]-1, apple[i][1]-1] for i in range(k)]
l = int(input())
d_list = [list(map(str, input().split())) for _ in range(l)]


def snack_move() :
    sec = 0
    snack = [(0, 0, 1)]
    r_idx = 0
    direction = {'D': [1, 2, 3, 0], 'L': [3, 0, 1, 2]}
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while snack and 0<=snack[-1][0]<n and 0<=snack[-1][1]<n:
        x,y,d = snack[-1][0],snack[-1][1],snack[-1][2]
        if sec==int(d_list[r_idx][0]): # 회전해야함
            r_d = direction[d_list[r_idx][1]][d]
            x+=moves[r_d][0]
            y+=moves[r_d][1]
            if (x,y,0) in snack or (x,y,1) in snack or (x,y,2) in snack or (x,y,3) in snack:
                return sec+1
            snack.append((x,y,r_d))
            r_idx+=1
            if r_idx>=len(d_list):
                r_idx=len(d_list)-1
        else :
            x+=moves[d][0]
            y+=moves[d][1]
            if (x, y, 0) in snack or (x, y, 1) in snack or (x, y, 2) in snack or (x, y, 3) in snack:
                return sec+1
            snack.append((x, y, d))

        if [x,y] not in apple:
            snack.pop(0)
        else :
            apple.remove([x,y])
        sec+=1
    return sec

print(snack_move())
