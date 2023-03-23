matriz = [['-', '-', '-'],
          ['-', '-', '-'],
          ['-', '-', '-']]

def showTab(matriz):
    for linha in matriz:
        print(linha)
        
def getMatriz(matriz):
    return matriz

def addPosition(linha, coluna, matriz, player):
    
    matriz[linha][coluna] = players(player)
    
        
def verifyPosition(linha, coluna, matriz, player):
    if matriz[linha][coluna] == '-' and matriz[linha][coluna] == '-':
        return True
    else:
        print('POSIÇÃO JA SELECIONADA!')
        print(f'Jogador {player} repita sua jogada')
        return False

    
def players(player):
    if player == 1:
        return 'x'
    elif player == 2:
        return 'o'
    else:
        return 'player nao existente'


def verLine(matriz, player, linha):
    
    tam = len(matriz)
    carac = players(player)
    cntCarac = 0
    coluna = 0
    
    #percorrendo as colunas da linha atual
    while coluna < tam:
        if matriz[linha][coluna] == carac:
            cntCarac += 1
        coluna += 1
        
    if cntCarac == 3:
        print(f'Jogador {player} ganhou')
        return True
    else:
        return False
        
        
def verColumn(matriz, player, coluna):
    tam = len(matriz)
    carac = players(player)
    cntCarac = 0
    linha = 0
    
    #percorrendo as colunas da linha atual
    while linha < tam:
        if matriz[linha][coluna] == carac:
            cntCarac += 1
        linha += 1
        
    if cntCarac == 3:
        print(f'Jogador {player} ganhou')
        return True
    else:
        return False

#def verMainDiag(matriz, player, linha, coluna):
    
#def verSecDiag(matriz, player, linha, coluna):

def verVelha(matriz):
    cntFreeSpace = 0
    tam = len(matriz)
    linha = 0
    
    while linha < tam:
        coluna = 0
        while coluna < tam:
            if matriz[linha][coluna] == '-':
                cntFreeSpace += 1
            coluna += 1
        linha += 1
        
    if cntFreeSpace == 0:
        print('DEU VELHA')
        return True
    else:
        return False
    
def verVictory(matriz, player, linha, coluna):
    
    if verLine(matriz, player, linha):
        return True
    
    elif verColumn(matriz, player, coluna):
        return True







def game(matriz):
    print()
    print('-=-=-=-= INICIANDO O JOGO -=-=-=-=')
    print()
    showTab(matriz)
    print()
    
    while True:
        player = 1
        while player <= 2:
            print()
            print(f'Jogador {player}')
            linha = int(input('linha: '))
            coluna = int(input('coluna: '))
            
            #se a posição ainda nao foi selecionada, adciona a nova posição
            #vai pro proximo jogador
            if verifyPosition(linha, coluna, matriz, player):
                
                addPosition(linha, coluna, matriz, player)
                showTab(matriz)
                
                verLine(matriz, player, linha)
                verColumn(matriz, player, coluna)
                verVelha(matriz)
                
                player += 1
                
            
          

game(matriz)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  