import pygame, sys
import numpy as np
#initialize pygame
pygame.init()

#variables
width= 600
height= 600
line_width= 10
crimson=(220, 20, 60)
line_color= (52, 235, 232)
board_rows=3
board_cols=3
circle_radius= 50
circle_width= 15
circle_color = (153, 102, 255)
square_color = (153, 102, 255)
square_width= 15
space= 55
player= 1
game_over= False

#display parameters
screen= pygame.display.set_mode( (width,height) )
pygame.display.set_caption( 'TIC_TAC_TOE ')
screen.fill( crimson )

board= np.zeros( (board_rows, board_cols))


#draw circles and squares
def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col]== 1:
                pygame.draw.circle(screen, circle_color, (int(col * 200 + 100), int(row * 200 + 100)),circle_radius,circle_width)
            elif board[row][col]== 2:
                pygame.draw.line(screen, square_color, (col*200+space, row*200+200-space), (col*200+200-space, row*200+space), square_width)
                pygame.draw.line(screen, square_color, (col*200+space, row*200+space), (col*200+200-space, row*200+200-space), square_width)
#draw the board
def line():
    pygame.draw.line( screen, line_color, (400,0), (400,600), line_width )
    pygame.draw.line( screen, line_color, (200,0), (200,600), line_width )
    pygame.draw.line( screen, line_color, (0,200), (600,200), line_width )
    pygame.draw.line( screen, line_color, (0,400), (600,400), line_width )


line()
#mark squares
def mark_squares(rows,cols,player):
    board[rows][cols]= player
#check if squares are available
def available_square(row,col):
    return board[row][col]== 0
#check if board is full
def isboardfull():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col]== 0:
                return False
    return True  
#check win conditions
def check_win(player):
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vertical_win_line(col, player)
            return True
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            horizontal_win_line(row, player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        diagonal_asc_line(player)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        diagonal_desc_line(player)
        return True
#the winning lines
def vertical_win_line(col,player):
    X= col*200 + 100
    if player == 1:
        color = circle_color
    elif player == 2:
        color = square_color
    pygame.draw.line(screen, color, (X,15), (X, height-15), 15)
def horizontal_win_line(row,player):
    Y = row*200 + 100
    if player == 1:
        color = circle_color
    elif player == 2:
        color = square_color
    pygame.draw.line(screen, color, (15, Y), (width-15, Y), 15)
def diagonal_asc_line(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = square_color
    pygame.draw.line(screen, color, (15, height-15), (width-15, 15), 15)
def diagonal_desc_line(player):
    if player == 1:
        color = circle_color
    elif player == 2:
        color = square_color
    pygame.draw.line(screen, color, (15, 15), (width-15, height-15), 15)
#press R to restart function
def restart():
    screen.fill(crimson)
    line()
    player = 1
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0
          
#function body for tic tac toe operation
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type== pygame.MOUSEBUTTONDOWN:
            mouseX= event.pos[0]
            mouseY= event.pos[1]

            clicked_row= int(mouseY//200)
            clicked_col= int(mouseX//200)

            if available_square(clicked_row, clicked_col) and not game_over:
                if player == 1:
                    mark_squares(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over= True
                    player= 2
                    draw_figures()
                elif player== 2:
                    mark_squares(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over= True
                    player= 1
                    draw_figures()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over= False
        
    pygame.display.update()
