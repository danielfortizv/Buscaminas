import matris as mts
import click2 as ck
import copy

def mapa_buscaminas():
    print('De que tamaño quieres tu juego')
    ancho = int(input('Ancho: '))
    alto = int(input('Alto: '))
    mapa = mts.crear_matris(ancho, alto)
    
    return ancho, alto, mapa

def mapa_minas():
    x,y,m = mapa_buscaminas()
    
    print('\nCon cuantas minas quieres jugar\n')
    maximo = x*y-1
    
    print('Puedes escoger desde 0 hasta',maximo)
    minas = int(input('Minas: '))
    
    print('\nPara poner una bandera, solo coloca la letra \"f\" '
          'despues de las cordenadas separadas por un espacio.')
    
    juego(m,minas)

def mensaje_vict_perd(n):
    vict = '||  FELICIDADES GANASTE  ||'
    perd = '||  BOOOM!! ||'
    if n == 1:
        men = vict
    else:
        men = perd
    print()
    print('||{0:-^78}||'.format(men))

def iniciar_juego():
    bn = '||  BIENVENIDO A BUSCAMINAS  ||'
    print('||{0:-^78}||'.format(bn))
    print()
    while True:
        mapa_minas()
        print('\n¿Quieres volver a jugar? (S/N)')
        if input('-> ').lower() != 's':
            break
    
def juego(tablero_blanco,minas):
    contador_minas = 0
    tablero_minas = copy.deepcopy(tablero_blanco)
    comprobante = True
    
    while comprobante:
        print()    
        mts.mapa(tablero_blanco)
        arr = input('Ingresa las cordenadas: ').split()
        j, i = int(arr[0])-1,int(arr[1])-1
        print()
        
        if tablero_minas == tablero_blanco:
            tablero_minas = mts.minas_matris(tablero_minas, minas, j, i)
        
        if len(arr) == 3 and ( tablero_blanco[i][j] == ' ' or tablero_blanco[i][j] == 'F' ):
            contador_minas = ck.flag(tablero_blanco, tablero_minas, contador_minas, i, j)
            if contador_minas == minas:
                comprobante = False
                n = 1
                mts.mapa(tablero_blanco)
                
        elif tablero_blanco[i][j] != ' ':
            print('Esa opción ya esta marcada')
        
        elif ck.perder(tablero_minas, i, j):
            b = ck.cords(tablero_blanco,tablero_minas, i, j)
            
            if b == 0:
                ck.cero(tablero_blanco, tablero_minas, i, j)
        
        else:
            comprobante = False
            n = 0
            mts.mapa(tablero_minas)
    
    mensaje_vict_perd(n)
    
iniciar_juego()