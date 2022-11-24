num = int(input())
stars = [['*' for _ in range(num)] for __ in range(num)]

def func(st_x,st_y,k):
    if k == 1 :
        return
    tmp = k//3

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                for a in range(st_x+tmp, st_x + tmp*2):
                    for b in range(st_y+tmp, st_y + tmp*2):
                        stars[a][b] = ' '
                
            func(st_x+tmp*i, st_y+tmp*j,k//3)


func(0,0,num)                
for tmp in stars:
    print(''.join(tmp))
