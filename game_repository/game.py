import pygame
#cores
amarelo = [200,200,20]
azul = [0,0,100]
verde =[0,200,0]
#tamanho da tela
w = 600
h= 470
#posição inicial
x = 100
y = 320
fps = pygame.time.Clock()
pygame.init()

#movimentando o personagem sob a tela
def imageview():
   
   background.blit(cenario,(0,0))
   background.blit(player,(x,y))
   text = font.render("SPACEBALL", True, verde)
   background.blit(text, [100, 200])
   pygame.display.update()
   fps.tick(60)

#carregando fonte
font = pygame.font.SysFont(None, 80)

#criando o plano de fundo
background = pygame.display.set_mode((w,h))
pygame.display.set_caption('spaceball')
#text = font.render('spaceball', True, verde)


#carregando imagem do personagem
cenario =pygame.image.load('images/space.png')
player = pygame.image.load('images/botao2.png')
player.convert()
rect = player.get_rect()


#looping do jogo

running = True
while running:
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         exit(0)
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
             x-=30
         if event.key == pygame.K_RIGHT:
            x+=30
     
      
      if x >=515:
         x = 515 
      if x <=0:
         x = 0
            
         #desenhando o personagem na tela
      imageview()