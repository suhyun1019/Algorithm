def solution(wallpaper):
    minX, minY, maxX, maxY = 50,50,0,0
    for i in range(len(wallpaper)) :
        for j in range(len(wallpaper[0])) :
            if wallpaper[i][j]=='#' :
                minX=min(minX, i)
                minY=min(minY, j)
                maxX=max(maxX, i+1)
                maxY=max(maxY, j+1)
    
    return [minX, minY, maxX, maxY]
