m = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]

def fila(tablero,i,j):
    contador = 0
    if i == 0:
        if tablero[1][j] == 'X':
            contador+=1
    elif i == len(tablero)-1:
        if tablero[len(tablero)-2][j] == 'X':
            contador+=1
    else:
        if tablero[i+1][j] == 'X':
            contador+=1
        if tablero[i-1][j] == 'X':
            contador+=1
    return contador

def columna(tablero,i,j):
    contador = 0
    if j == 0:
        if tablero[i][1] == 'X':
            contador+=1
    elif j == len(tablero[j])-1:
        if tablero[i][len(tablero[j])-2] == 'X':
            contador+=1
    else:
        if tablero[i][j+1] == 'X':
            contador+=1
        if tablero[i][j-1] == 'X':
            contador+=1
    return contador

def buscaminas(tablero,i,j):
    a = columna(tablero, i, j)
    b = fila(tablero, i, j)
    return a+b
