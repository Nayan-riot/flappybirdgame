import pygame
import random
pygame.init()

red = (200,0,0)
black = (0,0,0)
white = (233,233,233)

gamewidth = 400
gameheight = 600

gamewindow = pygame.display.set_mode((gamewidth,gameheight))
pygame.display.set_caption("Flappy bird")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,35)

bgimg = pygame.image.load("flappybirdbg.png")
bgimg = pygame.transform.scale(bgimg, (gamewidth,gameheight)).convert_alpha()

fbird = pygame.image.load("fbirdtrans.png")
fbird = pygame.transform.scale(fbird,(50,50)).convert_alpha()

fbirdwelcome = pygame.image.load("fbirdfrontpage.png")
fbirdwelcome = pygame.transform.scale(fbirdwelcome,(gamewidth,gameheight))

fobs = pygame.image.load("flapppyobstrans.png")
fobs = pygame.transform.scale(fobs,(70,520)).convert_alpha()

fobs2 = pygame.image.load("flapppyobstrans.png")
fobs2 = pygame.transform.scale(fobs2,(70,519))
fobs2 = pygame.transform.flip(fobs2,False,True)   

def score_scr(text,color,f,x,y):
    font = pygame.font.SysFont(None,f)
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,(x,y))

def welcome():  
    exit_game = False
    while not exit_game:
        gamewindow.fill((100,30,10))
        gamewindow.blit(fbirdwelcome,(0,0))
        score_scr("Developer:-",(0,0,0),30,170,520)
        score_scr("Nayan Adhikari",(100,0,0),30,147,550)
        # score_scr("!Press Enter to play!",(10,70,20),55,270,340)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
                    exit_game = True
        pygame.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False

    obstackle_x = 100
    obstackle_y = 300

    obstackle1_x = 300
    obstackle1_y = 300


    bird_x = 130
    bird_y = 100


    bird_valocity_y = 3

    obstackle_valocity_x = 2


    game_score = 0
    fps = 50




    while not exit_game:
        if game_over == True:
            gamewindow.fill(black)
            score_scr("!Game Over!",red,30,120,200)
            score_scr("press enter to play again",red,30,50,250)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game = True 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()                    

        else:
            for event in pygame.event.get():
            
                if event.type==pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        bird_y = bird_y - 60
                    if event.key == pygame.K_SPACE:
                        bird_valocity_y = 0
                        obstackle_valocity_x = 0

                        
            
            bird_y = bird_y + bird_valocity_y 
            obstackle_x = obstackle_x - obstackle_valocity_x
            obstackle1_x = obstackle1_x - obstackle_valocity_x        

            obstacleup1_x = obstackle_x
            obstacleup1_y = obstackle_y - 650

            obstacleup2_x = obstackle1_x
            obstacleup2_y = obstackle1_y - 650

            if abs(obstackle_x)<1:
                obstackle_x = 400
                obstackle_y = random.choice([250,200,300])


            if abs(obstackle1_x)<1:
                obstackle1_x = 400
                obstackle1_y = random.choice([350,280])
            
            if bird_x == obstackle_x or bird_x == obstackle1_x:
                game_score = game_score + 10

             
            gamewindow.fill(red)
            gamewindow.blit(bgimg,(0,0))
            pygame.draw.rect(gamewindow,black,(obstackle_x,obstackle_y,50,700))
            gamewindow.blit(fobs,(obstackle_x-8,obstackle_y-9)) 

            pygame.draw.rect(gamewindow,black,(obstackle1_x,obstackle1_y,50,700))
            gamewindow.blit(fobs,(obstackle1_x-8,obstackle1_y-9))

            pygame.draw.rect(gamewindow,black,(obstacleup1_x,obstacleup1_y,50,500))
            gamewindow.blit(fobs2,(obstacleup1_x-8,obstacleup1_y-10))
            
            pygame.draw.rect(gamewindow,black,(obstacleup2_x,obstacleup2_y,50,500))
            gamewindow.blit(fobs2,(obstacleup2_x-8,obstacleup2_y-10))
            
            pygame.draw.rect(gamewindow,black,(0,440,900,500))

            if bird_y==400 or bird_y < 0:
                game_over = True
            if abs(bird_x-obstackle_x)<30 and abs(bird_y-obstackle_y)<30:
                game_over = True
            if abs(bird_x-obstackle1_x)<30 and abs(bird_y-obstackle1_y)<30:
                game_over = True
            if abs(bird_x-obstacleup1_x)<30 and abs(bird_y-obstacleup1_y)<30:
                game_over = True
            if abs(bird_x-obstacleup2_x)<30 and abs(bird_y-obstacleup2_y)<30:
                game_over = True            
            pygame.draw.rect(gamewindow,black,(bird_x,bird_y,20,20))
            score_scr(f"Score = {game_score}",white,30,50,500)
            gamewindow.blit(fbird,(bird_x-10,bird_y-10))
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()