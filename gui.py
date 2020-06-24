import threading

import pygame
import pygame.gfxdraw
from PyQt5.QtWidgets import QWidget
import time
from damier import Damier
from simulation import Simulation

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
t = 0


class Gui(threading.Thread, QWidget):
    def __init__(self):
        threading.Thread.__init__(self)
        super().__init__()
        # tailles de cases
        self.width = 20
        self.height = 20
        # espace entre les cases
        self.margin = 5
        # les tableaux
        self.grid = []
        self.tableau = []
        self.tableau1 = []
        self.row = 0
        self.column = 0

        for row in range(20):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(40):
                self.grid[row].append(0)  # Append a cell

    def updateCell(self, x, y, valeur):
        self.grid[x-1][y-1] = valeur

    i = 0

    def run(self, n=-1, p=-1, x="", flag=1, g=-1, w=-1, y=-1):
        # Initialize pygame

        pygame.init()
        WINDOW_SIZE = [Damier.longueur(n), Damier.largeur(p)]
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(Damier.nom(x))

        # Loop until the user clicks the close button.
        done = False

        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        while not done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    column = pos[0] // (self.width + self.margin)
                    row = pos[1] // (self.height + self.margin)
                    # Set that location to one
                    self.grid[row][column] = 1
                    print("Click ", pos, "Grid coordinates: ", row, column)
                    self.tableau.append(row)
                    self.tableau1.append(column)


            # Set the screen background
            screen.fill(BLACK)

            # Draw the grid
            for row in range(20):
                for column in range(40):
                    color = WHITE
                    if self.grid[row][column] == 1:
                        color = GREEN
                    if self.grid[row][column] == 2:
                        color = RED
                    if self.grid[row][column] == 3:
                        color = BLACK
                    if self.grid[row][column] == 0:
                        color = WHITE
                    pygame.draw.rect(screen,
                                     color,
                                     [(self.margin + self.width) * column + self.margin,
                                      (self.margin + self.height) * row + self.margin,
                                      self.width,
                                      self.height])

            Simulation.cellulemorte(self)
            Simulation.cellulenaissante(self)
            Simulation.cellrestante(self)
            time.sleep(1)
            # Limit to 60 frames per second
            clock.tick(1)

            test = 0
            # Go ahead and update the screen with what we've drawn.

            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'

        # on exit.
        pygame.quit()
