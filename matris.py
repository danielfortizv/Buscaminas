import random as rnd

a = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
b = [[' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]

def crear_matris(ancho,largo):
    y = []
    for i in range(largo):
        y.append([' ' for i in range(ancho)])
    return y

def minas_matris(matris,minas,in_x,in_y):
    for _ in range(minas):
        x_cord = rnd.randrange(len(matris[0]))
        y_cord = rnd.randrange(len(matris))
        while matris[y_cord][x_cord] == 'X' or (x_cord == in_x and y_cord == in_y):
            x_cord = rnd.randrange(len(matris[0]))
            y_cord = rnd.randrange(len(matris))
        matris[y_cord][x_cord] = 'X'
    return matris

def mapa(matris):
    print(0,[f'{i+1}' for i in range(len(matris[0]))])
    print('-'*(len(matris[0])*5+2))
    num = 0
    for i in matris:
        num += 1
        print(num,i)
print(16*15*14*13*12*11*10*9*8*7*6*5*4*3*2)
print(1820*495*70)