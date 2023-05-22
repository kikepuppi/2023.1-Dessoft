
# pygame setup
import pygame

class Button():
    
    def __init__(self, x, y, imagem):
        self.image = imagem[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False
     
    def aparecer(self, screen, imagem):
        apertou = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.image = imagem[1]

            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                apertou = True

        if pygame.mouse.get_pressed()[0] == False:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))  

        return apertou
    
x = 1
y = 1
imagem = [1,2]
largura = 1
altura = 1
screen = 1

# criando o botao

butao = Button(x, y, imagem)
# aparecendo o botao

butao_acao = Button.aparecer(screen, imagem)

if butao_acao:
    print('muda de tela')
    # muda o state

# LETSGOOOOOOOOOOOOOOOOOOOOOO
# da pra por a berinjela como botao e nao muda o state, só soma 1 no dindin
# upgrade: gerar berinjela automatica += x

