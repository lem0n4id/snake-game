# write a snake game using pygame

import pygame
import random
import time

pygame.init()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# define display size
display_width = 600
display_height = 400

# define snake size
snake_block = 10

# define snake speed
snake_speed = 10

# define font size
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# define display
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake Game")

# define clock
clock = pygame.time.Clock()

# define snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])
        
# define message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width/6, display_height/3])
    
# define game loop
def gameLoop():
    
    # define game over
    game_over = False
    game_close = False
    
    # define snake position
    x1 = display_width/2
    y1 = display_height/2
    
    # define snake change
    x1_change = 0
    y1_change = 0
    
    # define snake list
    snake_List = []
    Length_of_snake = 1
    
    # define food position
    foodx = round(random.randrange(0, display_width - snake_block)/10.0)*10.0
    foody = round(random.randrange(0, display_height - snake_block)/10.0)*10.0
    
    # define score
    score = 0
    
    # game loop
    while not game_over:
        # game close
        while game_close == True:
            display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
            
            # game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        # snake movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                    
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                    
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                    
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                    
                # press q to quit
                elif event.key == pygame.K_q:
                    game_over = True
                
                # pause game
                elif event.key == pygame.K_p:
                    pause = True
                    while pause:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_p:
                                    pause = False
                        score_font = pygame.font.SysFont("comicsansms", 35)
                        value = score_font.render("Paused", True, red)
                        # render score
                        value1 = score_font.render("Score: " + str(score), True, red)
                        display.blit(value1, [0, 0])
                        display.blit(value, [display_width/3, display_height/5])
                        pygame.display.update()
                        clock.tick(5)
                        
        # snake out of boundary make it appear on the other side
        if x1 >= display_width:
            x1 = 0
        
        elif x1 < 0:
            x1 = display_width - snake_block
            
        elif y1 >= display_height:
            y1 = 0
            
        elif y1 < 0:
            y1 = display_height - snake_block
            
        # snake movement
        x1 += x1_change
        y1 += y1_change
        display.fill(white)
        
        # draw food
        pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
        
        # snake list
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        # snake length
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
            
        # snake eat food
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
                
        # draw snake
        snake(snake_block, snake_List)
        
        # update display
        pygame.display.update()
        
        # snake eat food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block)/10.0)*10.0
            foody = round(random.randrange(0, display_height - snake_block)/10.0)*10.0
            Length_of_snake += 1
            
        # define clock
        clock.tick(snake_speed)
        
    # quit game
    pygame.quit()
    quit()
    
# main menu
def main_menu():
    
    # make background white
    display.fill(white)
    
    # show button to start game
    start_button = pygame.Rect(0, 0, 200, 50)
    start_button.center = (display_width/2, display_height/2)
    pygame.draw.rect(display, blue, start_button)
    start_text = font_style.render("Start Game", True, white)
    display.blit(start_text, [display_width/2 - 50, display_height/2 - 10])
    
    # show button to quit game
    quit_button = pygame.Rect(0, 0, 200, 50)
    quit_button.center = (display_width/2, display_height/2 + 100)
    pygame.draw.rect(display, blue, quit_button)
    quit_text = font_style.render("Quit Game", True, white)
    display.blit(quit_text, [display_width/2 - 50, display_height/2 + 90])
    
    # show game title and author "Snake Game by Lenin"
    title_text = font_style.render("Snake Game by Lenin", True, black)
    display.blit(title_text, [display_width/2 - 100, display_height/2 - 200])
    
    # draw illustration of snake without an image
    pygame.draw.rect(display, black, [display_width/2 - 50, display_height/2 - 150, snake_block, snake_block])
    pygame.draw.rect(display, black, [display_width/2 - 40, display_height/2 - 150, snake_block, snake_block])
    pygame.draw.rect(display, black, [display_width/2 - 30, display_height/2 - 150, snake_block, snake_block])
    pygame.draw.rect(display, black, [display_width/2 - 20, display_height/2 - 150, snake_block, snake_block])
    pygame.draw.rect(display, black, [display_width/2 - 10, display_height/2 - 150, snake_block, snake_block])
    pygame.draw.rect(display, black, [display_width/2, display_height/2 - 150, snake_block, snake_block])
    pygame.draw.rect(display, black, [display_width/2 + 10, display_height/2 - 150, snake_block, snake_block])
    pygame.draw.rect(display, black, [display_width/2 + 20, display_height/2 - 150, snake_block, snake_block])
    pygame.draw.rect(display, black, [display_width/2 + 30, display_height/2 - 150, snake_block, snake_block])
    pygame.draw.rect(display, black, [display_width/2 + 40, display_height/2 - 150, snake_block, snake_block])
    pygame.draw.rect(display, black, [display_width/2 + 50, display_height/2 - 150, snake_block, snake_block])
    

    
    
    
    # update display
    pygame.display.update()
    
    # main menu loop
    while True:
        
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            # check if mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check if mouse is clicked on start button
                if start_button.collidepoint(event.pos):
                    gameLoop()
                    
                # check if mouse is clicked on quit button
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    quit()
                    
# call main menu
main_menu()
