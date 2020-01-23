"""
Tic Tac Toe game

Alexandre Salem Gagne Lamouri

February 5th 2019
"""
import pygame

# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [400, 400]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Tic Tac Toe")


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 



class Board:
    def __init__(self, width, height, margin):
        '''Build a new game board with tile width, height and margin'''
        self.width = width
        self.height = height
        self.margin = margin
        
        self.grid = []
        for row in range(3):
            self.grid.append([])
            for column in range(3):
                self.grid[row].append(0)
                
        self.update()
                
    def get_grid(self):
        return self.grid
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_margin(self):
        return self.margin
                
    def update(self):
        ''' Update game board'''
        screen.fill(BLACK)
        
        for row in range(3):
            for column in range(3):
                
                if self.grid[row][column] == 1:
                    color = GREEN
                    
                elif self.grid[row][column] == 2:
                    color = RED
                    
                else:
                    color = WHITE
                    
                pygame.draw.rect(screen,
                                 color,
                                 [(self.margin + self.width) * column + self.margin,
                                  (self.margin + self.height) * row + self.margin,
                                  self.width,
                                  self.height])     
                
        pygame.display.flip()
        
    def is_win(self, player):
        
        # Check horizontal
        for row in range(3):
            if grid[row][0] == player and grid[row][1] == player and grid[row][2]:
                return True
            
        # Check vertical
        for column in range(3):
            if grid[0][column] == player and grid[1][column] == player and grid[2][column]:
                return True  
            
        # Check diagonal (top left to bottom right)
        if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
            return True
        
        # Check diagonal (top right to bottom left)
        if grid[2][0] == player and grid[1][1] == player and grid[0][2] == player:
            return True       
        
        return False
        
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize Player and Board
player = 1
board = Board(100,100,25)

done = False

# Main Loop
while not done:
    for event in pygame.event.get(): 
        
        if event.type == pygame.QUIT: 
            done = True 
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            grid = board.get_grid()
            width = board.get_width()
            height = board.get_height()
            margin = board.get_margin()
            
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            
            # If tile is unclaimed
            if grid[row][column] == 0:
                grid[row][column] = player
                print("Tile", row, column,"claimed by Player", player)
                
                # Check victory
                if board.is_win(player):
                    print("Player", player, "won the game!")
                    pygame.time.delay(6000)
                    done = True
                  
                
                else:
                    #Switch Players
                    if player == 1:
                        player = 2
                    elif player == 2:
                        player = 1
                        
                    #Update board
                    board.update()
                
            # If tile is claimed   
            else:
                print("Tile already claimed by Player ", grid[row][column])


clock.tick(60)

pygame.quit()