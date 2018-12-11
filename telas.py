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
    textRect.center = (x+width/2, y+height/2)
    
    pygame.draw.rect(screen, btn_color, (x, y, width, height))
    screen.blit(textSurf, textRect)

    mousePos = pygame.mouse.get_pos()
    if x<mousePos[0]<x+width and y<mousePos[1]<y+height and onImage != None:
        screen.blit(onImage, (x-45 ,y-4 ))

def mouseCollide(tela, isDisabled = False):
    mousePos = pygame.mouse.get_pos()
    x = (ScreenWidth-btnRectSize[0])/2 #Para botoes que se encontram no meio da tela
    if tela == "Menu":
        if x < mousePos[0] < x+btnRectSize[0] and (ScreenHeight/4)+30<mousePos[1]<(ScreenHeight/4)+30+btnRectSize[1]:
            Teste.main(0)
        elif x < mousePos[0] < x+btnRectSize[0] and (ScreenHeight/4)+3*30 < mousePos[1] < (ScreenHeight/4)+3*30+btnRectSize[1]:
            OptionsScreen()
        elif x < mousePos[0] < x+btnRectSize[0] and (ScreenHeight/4)+5*30 < mousePos[1] < (ScreenHeight/4)+5*30+btnRectSize[1]:
            pygame.quit()
            quit()
    elif tela == "GameOver":
        if int(0.5*btnRectSize[0]) < mousePos[0] < int(1.5*btnRectSize[0]) and ScreenHeight-int(1.5*btnRectSize[1]) < mousePos[1] < ScreenHeight-int(0.5*btnRectSize[1]):
            MenuScreen()
        elif ScreenWidth-int(1.5*btnRectSize[0]) < mousePos[0] < ScreenWidth-int(0.5*btnRectSize[0]) and ScreenHeight-int(1.5*btnRectSize[1]) < mousePos[1] < ScreenHeight-int(0.5*btnRectSize[1]) and isDisabled == False:
            Teste.main(0)
    elif tela == "Opcoes":
        if x < mousePos[0] < x+btnRectSize[0] and (ScreenHeight/4)+30<mousePos[1]<(ScreenHeight/4)+30+btnRectSize[1]:
            ControlsScreen()
        elif x < mousePos[0] < x+btnRectSize[0] and (ScreenHeight/4)+3*30 < mousePos[1] < (ScreenHeight/4)+3*30+btnRectSize[1]:
            print("O jogo")
        elif x < mousePos[0] < x+btnRectSize[0] and (ScreenHeight/4)+5*30 < mousePos[1] < (ScreenHeight/4)+5*30+btnRectSize[1]:
            CreditsScreen()
        elif x < mousePos[0] < x+btnRectSize[0] and (ScreenHeight/4)+7*30 < mousePos[1] < (ScreenHeight/4)+7*30+btnRectSize[1]:
            MenuScreen()
    elif tela == "Controles":
        if ScreenWidth-btnRectSize[0]-10 < mousePos[0] < ScreenWidth-10 and 10<mousePos[1]<10+btnRectSize[1]:
            OptionsScreen()

def MenuScreen():
    pygame.font.init()   
    menu = True
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                mouseCollide("Menu")


        btnFont = pygame.font.Font("freesansbold.ttf", 150)
        textSurf, textRect = text_objects("K.A.z.", btnFont, DarkGreen)
        textRect.center = (ScreenWidth/2, 100)
        screen.blit(MenuBG,(0,0))
        screen.blit(textSurf, textRect)
        
#<g: GERANDO OS BOTÕES>------------------------------------------
        
        button("Jogar", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+1*30, btnRectSize[0], btnRectSize[1], DarkGreen, White, selectedOption)
        button("Opçoes", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+3*30, btnRectSize[0], btnRectSize[1], DarkGreen, White, selectedOption)
        button("Sair", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+5*30, btnRectSize[0], btnRectSize[1], DarkGreen, White, selectedOption)

#-------------------------------------------------------------</g
        
        pygame.display.update()
        clock.tick(15)

def GameoverScreen():
    pygame.font.init()   
    menu = True

    timeTot = 15
    timeOut = 1300     #tempo da contagem em ms
    contDelay = pygame.time.get_ticks()
    contTimer = 10

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                if contTimer >= 0:
                    mouseCollide("GameOver")
                else:
                    mouseCollide("GameOver", True)

        btnFont = pygame.font.Font("freesansbold.ttf", 100)
        textSurf, textRect = text_objects("Continuar?", btnFont, Black)
        textRect.center = (ScreenWidth/2, 3*ScreenHeight/4-20)
        screen.blit(GameOverBG,(0,0))
        screen.blit(textSurf, textRect)
        
#<g: GERANDO OS BOTÕES>------------------------------------------
        
        button("Menu", btnRectSize[0]/2, ScreenHeight-int(1.5*btnRectSize[1]), btnRectSize[0], btnRectSize[1], Red, Black, selectedOption)

        contDelayAux = pygame.time.get_ticks()
        contTimer = timeTot - int((contDelayAux-contDelay)/timeOut)
        if contTimer < 0 :
            contTimer = -1
            button("-.-", ScreenWidth-int(1.5*btnRectSize[0]), ScreenHeight-int(1.5*btnRectSize[1]), btnRectSize[0], btnRectSize[1], DarkGreen, Black, None)
        else:
            button(str(contTimer), ScreenWidth-int(1.5*btnRectSize[0]), ScreenHeight-int(1.5*btnRectSize[1]), btnRectSize[0], btnRectSize[1], Green, DarkGreen, selectedOption)        


#-------------------------------------------------------------</g
        
        pygame.display.update()
        clock.tick(15)

def OptionsScreen():
    pygame.font.init()    
    menu = True

    j = 0
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                mouseCollide("Opcoes")

        btnFont = pygame.font.Font("freesansbold.ttf", 80)
        textSurf, textRect = text_objects("Opções", btnFont, Black)
        textRect.center = (ScreenWidth/2, 100)
        screen.blit(OpcoesBG,(0,0))
        screen.blit(textSurf, textRect)
        
#<g: GERANDO OS BOTÕES>------------------------------------------
        
        button("Controles", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+1*30, btnRectSize[0], btnRectSize[1], Green, DarkGreen, selectedOption)
        button("-.-", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+3*30, btnRectSize[0], btnRectSize[1], Green, DarkGreen, None)
#<t:Jogo>
        mousePos = pygame.mouse.get_pos()
        if (ScreenWidth-btnRectSize[0])/2 < mousePos[0] < (ScreenWidth-btnRectSize[0])/2+btnRectSize[0] and (ScreenHeight/4)+3*30 < mousePos[1] < (ScreenHeight/4)+3*30+btnRectSize[1]:
            if j == 0:
                jITimer = pygame.time.get_ticks()
                j = 1
            jIITimer = pygame.time.get_ticks()
            if ((jIITimer-jITimer+1)/1000) <= 0.2:
                button("o jogo", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+3*30, btnRectSize[0], btnRectSize[1], Green, DarkGreen, None)
        #Só por zuar (Deixar ou não, eis a dúvida...)
#</t:Jogo>
        
        button("Créditos", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+5*30, btnRectSize[0], btnRectSize[1], Green, DarkGreen, selectedOption)
        button("Voltar", (ScreenWidth-btnRectSize[0])/2, (ScreenHeight/4)+7*30, btnRectSize[0], btnRectSize[1], Green, DarkGreen, selectedOption)

#-------------------------------------------------------------</g
        
        pygame.display.update()
        clock.tick(15)

def ControlsScreen():
    pygame.font.init()    
    menu = True
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                mouseCollide("Controles")

        screen.blit(ControlesBG,(0,0))
        
#<g: GERANDO OS BOTÕES>------------------------------------------
        
        button("Voltar", ScreenWidth-btnRectSize[0]-10, 10, btnRectSize[0], btnRectSize[1], Green, DarkGreen, None)

#-------------------------------------------------------------</g
        
        pygame.display.update()
        clock.tick(15)

def CreditsScreen():
    pygame.font.init()    
    menu = True

    yIni = ScreenWidth - 200
    creditsSpeed = 7
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.MOUSEBUTTONDOWN:
                mouseCollide("Creditos")

        screen.blit(CreditosBG,(0,0))
        if yIni > -1000:
            yIni = yIni - creditsSpeed
            screen.blit(CreditosLetras,(0,yIni))
        else:
            pygame.time.delay(2000)
            OptionsScreen()
        
#<g: GERANDO OS BOTÕES>------------------------------------------
        
        #button("Voltar", ScreenWidth-btnRectSize[0]-10, 10, btnRectSize[0], btnRectSize[1], Green, DarkGreen, None)

#-------------------------------------------------------------</g
        
        pygame.display.update()
        clock.tick(15)

pygame.init()
screenSize = [ScreenWidth, ScreenHeight]
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("K.A.Z.")
clock = pygame.time.Clock()
    
MenuScreen()
#OptionsScreen()
#ControlsScreen()
#GameoverScreen()
