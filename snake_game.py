# subscribed by nitish kumar
# https://m.facebook.com/story.php?story_fbid=2746412395598393&id=100006889785546


import pygame
import random
import sys
import os
pygame.init()

white=(255,255,255) #defining color between 0-255 and these are the rgb values
red=(255,0,0)
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
screen_width=500
screen_height=500
font=pygame.font.SysFont(None,24)
clock = pygame.time.Clock()
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

#creating window
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("SnakeWithKishan")
pygame.display.update() #to update the screen whenever any change happpens

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])
def plot_snake(gameWindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, black, [x,y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(green)
        text_screen("Press Enter to start the game...", blue, 100, 200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(60)


def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 35
    snake_size = 10
    score = 0

    fps = 30
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over!!Press enter to continue..",red,100,220)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=5
                        velocity_y=0
                    if event.key == pygame.K_DOWN:
                        velocity_y=+5;
                        velocity_x=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-5
                        velocity_y=0
                    if event.key == pygame.K_UP:
                        velocity_y=-5
                        velocity_x=0
            snake_x=snake_x+velocity_x

            snake_y=snake_y+velocity_y
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score+=1

                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snk_length+=5
            if score>int(hiscore):
                hiscore=score

            gameWindow.fill(white)
            text_screen("score: " + str(score * 10) + "  Highscore: "+str(hiscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_length:
                del snk_list[0]

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                print("game over")
            #pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()
