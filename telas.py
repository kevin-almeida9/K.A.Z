from constantes import *
import Teste
import pygame

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def button(msg, x, y, width, height, btn_color, text_color, onImage):
    btnFontSize = int(height * 0.8)
    btnFont = pygame.font.Font("freesansbold.ttf", btnFontSize)
    textSurf, textRect = text_objects(msg, btnFont, text_color)

    textRect.center = (x+btnRectSize[0]/2, y+btnRectSize[1]/2)
    pygame.draw.rect(screen, btn_color, (x, y, width, height))
    screen.blit(textSurf, textRect)

    mousePos = pygame.mouse.get_pos()
    if x<mousePos[0]<x+width and y<mousePos[1]<y+height:
        screen.blit(onImage, (x-45 ,y-4 ))
    
def main():

    
    pygame.font.init()
    

    ScreenImage = pygame.Surface(screenSize, pygame.SRCALPHA)

    fontPadrao = pygame.font.get_default_font()
    fontSize = 200
    
    fontTeste = pygame.font.SysFont(fontPadrao, fontSize)
    
    
    menu = True
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                print('-------')
                print(((ScreenWidth-btnRectSize[0])/2), mousePos[0], (ScreenWidth+btnRectSize[0])/2 )
                print((ScreenHeight/4)+1*30, mousePos[1], (ScreenHeight/4)+1*30+btnRectSize[1])

        Text = fontTeste.render('K.A.Z.', 1, DarkGreen)
        screen.blit(MenuBG,(0,0))
        screen.blit(Text, ((ScreenWidth/2)-fontSize, 30))

                
        #btnText = btnFont.render('Jogar', 1, White)
        #pygame.draw.rect(screen, DarkGreen, ((ScreenWidth/2-90), (ScreenHeight/4)+1*30, 180, 45))
        #screen.blit(btnText, ((ScreenWidth/2)-btnSize, (ScreenHeight/4)+1*30+8))
        
        #btnText = btnFont.render('Opções', 1, White)
        #pygame.draw.rect(screen, DarkGreen, ((ScreenWidth/2-90), (ScreenHeight/4)+3*30, 180, 45))
        #screen.blit(btnText, ((ScreenWidth/2)-btnSize, (ScreenHeight/4)+3*30+8))

        #btnText = btnFont.render('Sair', 1, White)
        #pygame.draw.rect(screen, DarkGreen, ((ScreenWidth/2-90), (ScreenHeight/4)+5*30, 180, 45))
        #screen.blit(btnText, ((ScreenWidth/2)-btnSize, (ScreenHeight/4)+5*30+8))

        
#<g: GERANDO OS BOTÕES>------------------------------------------
        #i = 1

        button("Jogar", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+1*30, btnRectSize[0], btnRectSize[1], DarkGreen, White, selectedOption)
        button("Opçoes", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+3*30, btnRectSize[0], btnRectSize[1], DarkGreen, White, selectedOption)
        button("Sair", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+5*30, btnRectSize[0], btnRectSize[1], DarkGreen, White, selectedOption)
        #while i <= 5:
         #   button(i)
          #  i+=2
#-------------------------------------------------------------</g>
            
        
            
        pygame.display.update()
        clock.tick(15)

pygame.init()
screenSize = [ScreenWidth, ScreenHeight]
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("K.A.Z.")
clock = pygame.time.Clock()
    
main()
