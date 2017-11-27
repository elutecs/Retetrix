
import pygame,sys,time,threading
from pygame.locals import*

from random import randint

class Cuadro(object):

    x,y = 0,9
    position = [[1,0,0],[0,1,0],[0,0,1]]
    def avanzar(self):
        self.x+=1
    def girar(self):
        lista = [[0,0,0],[0,0,0],[0,0,0]]
        limite1 = 0
        for i in range(3):
            limite2 = 2
            for j in range(3):
                lista[i][j] = self.position[limite2][limite1]
                limite2-=1
            limite1+=1
        self.position = lista
    def arriba(self,matriz):
        bandera  = False
        for i in range(3):
            for j in range(3):
                if self.position[i][j]==1:
                    if (matriz[self.y+i-1][self.x+j]==-1):
                        bandera = True
        if bandera==False:
            self.y-=1
    def abajo(self,matriz):
        bandera  = False
        for i in range(3):
            for j in range(3):
                if self.position[i][j]==1:
                    if (matriz[self.y+i+1][self.x+j]==-1):
                        bandera = True
        if bandera==False:
            self.y+=1

def crearMatriz(n,m):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            if i == (n-1) or i == 2 or j == m//2: matriz[i].append(-1)
            else : matriz[i].append(0)
    return matriz

def dibujarMatriz(ventana,matriz,color):
    for i in range(3,len(matriz)-1):
        for j in range(1,len(matriz[0])-1):
            if matriz[i][j]==1 : pygame.draw.rect(ventana,(color[0],color[1],color[2],0),(j*25+10,i*25-30,25,25),0)
            elif matriz[i][j]==-1 : pygame.draw.rect(ventana,(0,0,0,0),(j*25+10,i*25-30,25,25),0)
            pygame.draw.rect(ventana,(0,0,0,0),(j*25+10,i*25-30,25,25),2)
            pass
        pass

def dibujarBorrar(matriz,cuadrito, bandera, grabar):
    limite1 = 0
    for i in range( cuadrito.y,(len(cuadrito.position)+cuadrito.y)):
        limite2 = 0
        for j in range( cuadrito.x,(len(cuadrito.position[0])+cuadrito.x)) :
            if bandera==True and grabar==False and cuadrito.position[limite1][limite2]==1:
                matriz[i][j]=cuadrito.position[limite1][limite2]
            elif bandera==False and grabar==False and cuadrito.position[limite1][limite2]==1:
                matriz[i][j]=0
            elif grabar==True and cuadrito.position[limite1][limite2]==1:
                matriz[i][j]=-1
            limite2+=1
        limite1+=1

def colorRandom():
    nuevo = [randint(0,150),randint(0,150),randint(0,150)]
    return nuevo

def condicion(m,c,color):
    bandera = False
    for i in range(3):
        for j in range(3):
            if c.position[i][j]==1:
                if m[c.y+(i)][c.x+(j+1)]==-1: #antes checkeaba si habian piezas abajo, ahora si estan al costado
                    bandera = True
    if bandera ==True:
        dibujarBorrar(m,c,False,True)
        c.y,c.x = 9,0
        c.position = random()
        color = colorRandom()
    return color

def random():
    lista1 = [[0,1,0],[1,1,0],[1,0,0]]
    lista2 = [[0,0,0],[1,1,0],[1,1,0]]
    lista3 = [[0,0,0],[0,0,1],[1,1,1]]
    lista4 = [[0,0,1],[0,0,1],[0,0,1]]
    lista5 = [[0,0,0],[0,1,0],[0,0,0]]
    lista6 = [[0,0,0],[0,1,0],[1,1,1]]
    lista7 = [[1,0,0],[1,1,0],[0,1,0]]
    lista8 = [[0,1,0],[0,1,0],[0,0,0]]
    lista9 = [[1,0,1],[1,1,1],[0,0,1]]
    lista10= [[1,0,1],[1,0,1],[1,1,1]]
    lista11= [[1,1,1],[0,0,1],[0,0,1]]
    lista12= [[1,1,1],[0,1,1],[0,0,1]]
    lista13= [[1,1,0],[1,1,0],[0,1,0]]
    lista14= [[1,1,1],[1,1,1],[1,1,1]]
    lista15= [[1,1,1],[1,1,0],[0,1,0]]
    lista16= [[0,1,0],[1,1,1],[0,1,0]]
    lista17= [[0,0,0],[0,1,0],[0,0,0]]
    lista18= [[0,0,1],[0,0,1],[0,0,1]]
    lista19= [[0,1,0],[0,1,0],[0,0,0]]
    lista20= [[0,0,0],[0,1,0],[0,0,0]]
    lista21= [[0,0,1],[0,0,1],[0,0,1]]
    lista22= [[0,0,0],[0,1,0],[0,0,0]]
    lista23= [[0,0,0],[0,1,0],[0,0,0]]
    lista24= [[0,0,0],[0,1,0],[0,0,0]]
    lista25= [[0,0,0],[0,1,0],[0,0,0]]

    listota = [lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8,lista9,lista10,lista11,lista12,
               lista13,lista14,lista15,lista16,lista17,lista18,lista19,lista20,lista21,lista22,lista23,lista24,lista25]
    return listota[randint(0,len(listota)-1)]



def revisarMatriz(matriz):
    indice =-1
    for i in range(1,(len(matriz[0])//2)):
        bandera = False
        for j in range(3,len(matriz)-1):
            if matriz[j][i]==0: bandera = True
        if bandera==False:
            print("Tienes 10 puntos mas!!!")


            for n in reversed(range(1,(i+1))):
                for j in range(3,len(matriz)-1):
                    matriz[j][n] = matriz[j][n-1]



def imprimir(matriz):
    for i in range(len(matriz)):
        print(matriz[i])



def principal():

    izquierda = True
    ventana = pygame.display.set_mode((685,620))
    matriz = crearMatriz(16,53)
    cuadrito,contador,bandera,color = Cuadro(),0,False,[1,1,255]
    cuadrito.position = random()

    while True:
        ventana.fill((255,255,255,255))
        dibujarBorrar(matriz,cuadrito,True,False)  #pintar
        dibujarMatriz(ventana,matriz,color)        #dibujar
        dibujarBorrar(matriz,cuadrito,False,False) #borrar
        revisarMatriz(matriz)                       #revisar
        color = condicion(matriz,cuadrito,color)
        if contador > 10 or bandera==True:
            cuadrito.avanzar()
            contador=0
        contador+=1
        for events in pygame.event.get():
            if events.type==QUIT:
                pygame.quit()
                sys.exit()
            elif events.type==KEYDOWN:

                if events.key==K_UP:
                    cuadrito.arriba(matriz)
                elif events.key==K_DOWN:
                    cuadrito.abajo(matriz)
                #acelerar y girar
                elif events.key==K_RIGHT:
                    if izquierda:
                        bandera=True
                    else:
                        cuadrito.girar()
                elif events.key==K_LEFT:
                    if izquierda:
                        cuadrito.girar()
                    else:
                        bandera=True

            elif events.type==KEYUP:
                if events.key==K_RIGHT and izquierda:
                    bandera=False
                elif events.key==K_LEFT and (not izquierda):
                    bandera=False
        pygame.display.update()
        time.sleep(.08)

def main():
    principal()
main()
