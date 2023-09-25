import pygame

pygame.init()  
pygame.display.set_caption('adding images')  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loo

#CONSTANTS



timer = 400

score = 0
scoretoggle = False
scored = False
mxpos = 0
mypos = 0
xpos = 500 #xpos of player
ypos = 200 #ypos of player
mousePos = (mxpos, mypos)
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
MRight = False
MLeft = False

#Basket Variables
Bxpos = 100
Bypos = 500
Axpos = 100
Aypos = 500
while not gameover and timer >= 0: #GAME LOOP############################################################
    clock.tick(60) #FPS
    timer -=1
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
        
        if event.type == pygame.MOUSEMOTION: #check if mouse moved
            mousePos = event.pos #refreshes mouse position
            print("mouse position: (",mousePos[0]," , ",mousePos[1], ")")

        if event.type == pygame.MOUSEBUTTONDOWN:
            vy -= 10
            if mousePos[0] >= 400:
                 vx += 1
            if mousePos[0] <= 400:
                 vx -=1
          

    
    



    
 
#PHYSICS----------------------------------------------------------------------
  
    


    if xpos < 0:
        xpos = 799

    elif xpos > 800:
        xpos = 1


    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
    if scoretoggle == False:
        if xpos <= Bxpos+10 and ypos <= Bypos+10:
            if xpos > Bxpos-20 and ypos >= Bypos-20:
                print("hit")
                print(score)
                scored = True
                timer = 400
    else:
        if xpos >= Bxpos+30 and ypos >= Bypos-10:
            if xpos < Bxpos+45 and ypos <= Bypos+20:
                print("hit")
                print(score)
                scored = True
                timer = 400

#SCORING--------------------------------------------------------
    if scored == True:
        if scoretoggle == False:
            scoretoggle = True
            score += 1
            Axpos = 700
            Bxpos = 700
            scored = False
        elif scoretoggle == True:
            scoretoggle = False
            score += 1
            Axpos = 100
            Bxpos = 100
            scored = False
        
    
    
       
        #gravity
    if ypos < 699:
        vy+=.4 #notice this grows over time, aka ACCELERATION
           

    #update player position
    xpos+=vx 
    ypos+=vy

    screen.fill((0,0,0)) #wipe screen so it doesn't smear
        
    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 10)

    pygame.draw.rect(screen,(255,0,0),(Axpos,Aypos,35,15))
    if scoretoggle == True:
        pygame.draw.rect(screen,(255,0,0),(Bxpos+35,Bypos-50,8,60))
    else:
        pygame.draw.rect(screen,(255,0,0),(Bxpos-8,Bypos-50,8,60))
    
    #pygame.draw.rect(screen,(255,0,0),(Axpos+33,Aypos-50,8,60))
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(str(score), 1 ,(255, 0, 0))
    text_surface2 = my_font.render(str(timer), 1 ,(255, 0, 0))
    screen.blit(text_surface, (0,0))
    screen.blit(text_surface2, (0,40))
    pygame.display.flip()#this actually puts the pixel on the screen
    



#end game loop------------------------------------------------------------------------------
pygame.quit()
