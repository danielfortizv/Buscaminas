m = [[' ', 'X', ' ', 'X'],
     ['X', ' ', 'A', ' '],
     [' ', 'X', 'X', ' '],
     ['X', ' ', ' ', 'X']]

def counter(tbl, x, z, i, j):
    cont = 0
    c = j
    
    for a in range(i,x):
        for b in range(j,z):
    
            if tbl[a][b] == 'X':
                cont+=1
        j=c
    return cont

def buscaminas(tablero, i, j):
    contador = 0
    j-=1
    i-=1
    x = i + 3
    z = j + 3
    
    if i == -1:
        i+= 1
    if i == len(tablero)-2:
        x-= 1
    if j == -1:
        j+= 1
    if j == len(tablero[i+1])-2:
        z-= 1
    
    contador+= counter(tablero, x, z, i, j)
    
    return contador

def perder(tablero,i,j):
    respuesta = True
    
    if tablero[i][j] == 'X':
        respuesta = False
    
    return respuesta

def flag(tablero_blanco, tablero_minas, cont, i, j):
    if tablero_blanco[i][j] == 'F':
        tablero_blanco[i][j] = ' '
        
        if tablero_minas[i][j] == 'X':
            cont -= 1
        else:
            cont += 1
    
    else:
        tablero_blanco[i][j] = 'F'
        
        if tablero_minas[i][j] == 'X':
            cont += 1
        else:
            cont -= 1
            
    return cont

def cords(tablero_blanco, tablero_minas, i, j):
    valor = buscaminas(tablero_minas,i,j)
    tablero_blanco[i][j] = str(valor)
    
    return valor

def cero(tablero_blanco, tablero_minas, i, j):
    f,g = i,j
    j-=1
    i-=1
    x = i + 3
    z = j + 3
    
    if i == -1:
        i+= 1
    if i == len(tablero_minas)-2:
        x-= 1
    if j == -1:
        j+= 1 
    if j == len(tablero_minas[i+1])-2:
        z-= 1
    
    c = j
    
    for a in range(i,x):
        for b in range(j,z):
            
            if tablero_minas[a][b] == ' ' and (a != f or b != g) and tablero_blanco[a][b] == ' ':
                valor = cords(tablero_blanco,tablero_minas,a,b)
                
                if valor == 0:
                    cero(tablero_blanco,tablero_minas,a,b)
        j = c