'''
Initialize the class to make the
Node object
'''

# --- Modules --- #
import pygame

# --- Color Variables -- #
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0,255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0 , 255)
WHITE = (255, 255, 255)
GREY = (125, 125, 125)
BLACK = (0, 0, 0)

# --- Class --- #
class Node:
    def __init__(self, row, col, width):
        ''' Creates an individual node cube object '''
        self.row = row
        self.col = col
        self.width = width
        self.color = WHITE
        self.neighbors = []
        self.last_node = None
        self.shortest_dist = float('inf')
        self.f_score = float('inf')
        self.g_score = float('inf')
        self.h_score = float('inf')

    def __lt__(self, other):
        return False
    
    def __repr__(self):
        return f'This is Node [{self.row}][{self.col}]'

    def set_none(self):
        self.color = WHITE
    
    def set_wall(self):
        self.color = BLACK

    def set_explored(self):
        self.color = GREEN
    
    def set_start(self):
        self.color = ORANGE
    
    def set_end(self):
        self.color = BLUE
    
    def set_path(self):
        self.color = PURPLE
    
    def set_unexplored(self):
        self.color = RED
    
    def isWall(self):
        return self.color == BLACK
    
    def isEmpty(self):
        return self.color == WHITE
    
    def isStart(self):
        return self.color == ORANGE
    
    def isEnd(self):
        return self.color == BLUE
    
    def isExplored(self):
        return self.color == GREEN
    
    def isUnexplored(self):
        return self.color == RED

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.row * self.width, self.col * self.width, self.width, self.width))
    
    def update_neighbors(self, node_list, total_rows):
        if self.col > 0 and not node_list[self.row][self.col - 1].isWall(): # LEFT
            self.neighbors.append(node_list[self.row][self.col - 1])
        if self.col < total_rows - 1 and not node_list[self.row][self.col + 1].isWall(): # RIGHT
            self.neighbors.append(node_list[self.row][self.col + 1])
        if self.row > 0 and not node_list[self.row - 1][self.col].isWall():# UP
            self.neighbors.append(node_list[self.row - 1][self.col])
        if self.row < total_rows - 1 and not node_list[self.row + 1][self.col].isWall(): # DOWN
            self.neighbors.append(node_list[self.row + 1][self.col])
    
    def reset(self):
        self.color = WHITE
        self.neighbors = []
        self.last_node = None
        self.shortest_dist = float('inf')
        self.f_score = float('inf')
        self.g_score = float('inf')
        self.h_score = float('inf')