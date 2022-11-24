n = int(input())
paper_list = []
color_list = [0 for _ in range(3)]
for _ in range(n):
    paper_list.append(list(map(int,input().split())))

def func(st_x,st_y,n):
    paper_color = paper_list[st_x][st_y]
    for i in range(st_x, st_x+n):
        for j in range(st_y,st_y+n):
            if paper_list[i][j] != paper_color:
                for dir_x in range(3):
                    for dir_y in range(3):
                        func(st_x+dir_x*n//3,st_y+dir_y*n//3,n//3)
                return
    color_list[paper_color+1] += 1

func(0,0,n)
for color in color_list:
    print(color)