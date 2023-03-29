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

def whichPlayer(cntPlays):
    if cntPlays % 2 == 0:
        return 2
    else:
        return 1
    
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

def verMainDiag(matriz, player):
    tam = len(matriz)
    carac = players(player)
    cntCarac = 0
    linha = 0
    coluna = 0
    
    #percorrendo a diagonal principal
    while linha < tam:
        if matriz[linha][coluna] == carac:
            cntCarac += 1
            
        linha += 1
        coluna += 1
        
    if cntCarac == 3:
        print(f'Jogador {player} ganhou')
        return True
    else:
        return False
    
def verSecDiag(matriz, player):
    tam = len(matriz)
    carac = players(player)
    cntCarac = 0
    linha = 0
    coluna = 2
    
    #percorrendo a diagonal principal
    while linha < tam:
        if matriz[linha][coluna] == carac:
            cntCarac += 1
            
        linha += 1
        coluna -= 1
        
    if cntCarac == 3:
        print(f'Jogador {player} ganhou')
        return True
    else:
        return False

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
    
    elif verMainDiag(matriz, player):
        return True
    
    elif verSecDiag(matriz,player):
        return True
    
    else:
        return False




def game(matriz):
    print('-.-'*15)
    print('INTRUÇÕES')
    print()
    print('Apenas utilizar números de 0 a 2')
    print('As linhas e colunas da matriz são numeradas de 0 a 2')
    print()
    print('Ou seja, se você selecionar linha: 0  e coluna: 0 sua marcação será na primeira casa do tabuleiro')
    print('Dessa forma:')
    print('''
          ['x', '-', '-']
          ['-', '-', '-']
          ['-', '-', '-']''')
    print()
    print('-.-'*15)
    print()
    print('-=-=-=-= INICIANDO O JOGO -=-=-=-=')
    print()
    showTab(matriz)
    print()
    cntPlays = 1
    
    while True:
        
        player = whichPlayer(cntPlays)
        print()
        print(f'Jogador {player}')
        
        linha = int(input('linha: '))
        while linha > 2 or linha < 0:
            print('Selecione apenas numeros de 0 e 2')
            linha = int(input('linha: '))
            
        coluna = int(input('coluna: '))
        while coluna > 2 or coluna < 0:
            print('Selecione apenas numeros de 0 e 2')
            coluna = int(input('coluna: '))
        
        #se a posição ainda nao foi selecionada, adciona a nova posição
        #vai pro proximo jogador
        if verifyPosition(linha, coluna, matriz, player):
            
            addPosition(linha, coluna, matriz, player)
            showTab(matriz)
            
            #verificação de vitória
            if verVictory(matriz, player, linha, coluna):
                break
            elif verVelha(matriz):
                break
            cntPlays += 1
            
             
            
          

game(matriz)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  