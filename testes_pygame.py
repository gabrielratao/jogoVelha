import pygame

# Inicializa o Pygame
pygame.init()

# Define o tamanho da janela
tamanho_janela = (350, 350)
janela = pygame.display.set_mode(tamanho_janela)

# Define as cores que serão utilizadas
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)

# Define o tamanho e posição dos retângulos do tabuleiro
tamanho_casa = 100
margem = 10
posicoes_casas = []
for linha in range(3):
    for coluna in range(3):
        x = margem + coluna * (tamanho_casa + margem)
        y = margem + linha * (tamanho_casa + margem)
        posicoes_casas.append(pygame.Rect(x, y, tamanho_casa, tamanho_casa))

# Loop principal do jogo
jogo_ativo = True
while jogo_ativo:
    # Verifica eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_ativo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se o clique do mouse foi em alguma das casas do tabuleiro
            posicao_mouse = pygame.mouse.get_pos()
            for i, casa in enumerate(posicoes_casas):
                if casa.collidepoint(posicao_mouse):
                    # Muda a cor da casa que foi clicada
                    if i % 2 == 0:
                        cor = azul
                    else:
                        cor = vermelho
                    pygame.draw.rect(janela, cor, casa)
                    pygame.display.update() # atualiza a tela após o clique

    # Preenche a janela com a cor de fundo
    janela.fill(branco)

    # Desenha as linhas do tabuleiro
    for linha in range(4):
        pygame.draw.line(janela, preto, (margem, margem + linha * (tamanho_casa + margem)), (margem + 3 * (tamanho_casa + margem), margem + linha * (tamanho_casa + margem)), 5)
        pygame.draw.line(janela, preto, (margem + linha * (tamanho_casa + margem), margem), (margem + linha * (tamanho_casa + margem), margem + 3 * (tamanho_casa + margem)), 5)

    # Desenha as casas do tabuleiro
    for casa in posicoes_casas:
        pygame.draw.rect(janela, branco, casa, 5)

    # Atualiza a tela
    pygame.display.update()

# Encerra o Pygame
pygame.quit()
