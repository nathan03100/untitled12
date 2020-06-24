import time


class Simulation:

    def __init__(self):

        self.tableau = []
        self.tableau1 = []
        self.tableau2 = []
        self.tableau3 = []

        self.f = 0

    def cellulenaissante(self):

        for j in self.tableau:
            for i in self.tableau1:
                if self.grid[j][i] == 1 and not (i == 0 and j == 0):
                    self.f = j
                    self.grid[j + 1][i] = 1
                    self.grid[j - 1][i] = 1
                    self.grid[j][i + 1] = 1
                    self.grid[j][i - 1] = 1
                # cas particulier colone 0 et ligne zéro
                if i == 0 and j == 0:
                    self.grid[j + 1][i] = 1
                    self.grid[j - 1][i] = 0
                    self.grid[j][i + 1] = 1
                    self.grid[j][i - 1] = 0
                # cas particulier colone 0
                if i == 0 and not (i == 0 and j == 0):
                    self.grid[j + 1][i] = 1
                    self.grid[j - 1][i] = 1
                    self.grid[j][i + 1] = 1
                    self.grid[j][i - 1] = 0

    def cellrestante(self):
        for j in self.tableau:
            for i in self.tableau1:
                if self.grid[j][i] == 1:
                    self.grid[j][i] = 3



    def cellulemorte(self):

        for j in self.tableau:
            for i in self.tableau1:
                if self.grid[j][i] == 3:
                    if self.grid[j + 1][i] == 1 or 3:
                        if self.grid[j - 1][i] == 1 or 3:
                            if self.grid[j][i - 1] == 1 or 3:
                                if self.grid[j][i + 1] == 1 or 3:
                                    self.grid[j][i] = 0

