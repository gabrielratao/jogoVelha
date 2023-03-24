matriz = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]

def showTab(matriz):
    tam = len(matriz)
    linha = 0
    
    while linha < tam:
        coluna = 0
        while coluna < tam:
            print(matriz[linha][coluna])
            coluna += 1
        linha += 1
        
        
def abDiagonal(matriz):
    tam = len(matriz)
    diag = 1
    
    while diag < tam:
        linha = diag
        coluna = 0
        
        while linha < tam:
            print(matriz[linha][coluna])
            
            linha += 1
            coluna += 1
        diag += 1



def diagPri(matriz):
    tam = len(matriz)
    linha = 0
    coluna = 0
    while linha < tam:
        print(matriz[linha][coluna])
        linha += 1
        coluna += 1

def diagSec(matriz):
    tam = len(matriz)
    linha = 0
    coluna = 2
    while linha < tam:
        print(matriz[linha][coluna])
        linha += 1
        coluna -= 1
    
diagSec(matriz)   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    