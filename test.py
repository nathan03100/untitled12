import time
class Test:

    def init(self):

        self.tableau = []
        self.tableau1 = []
        self.tableau2=[]
        self.test=0



    def cellulenaissante(self,test=-1,coordonnee_x=0,coordonnee_y=0):
        coordonnee_x = 0
        while coordonnee_x <=2:
              print(2)
              coordonnee_y = 0
              while coordonnee_y <= 2:
                    print(2)
                    if self.grid[coordonnee_x][cordonnee_y] == 1:
                        self.grid[coordonnee_x + 1][cordonnee_y] = 1
                        self.grid[coordonnee_x - 1][cordonnee_y] = 1
                        self.grid[coordonnee_x][cordonnee_y + 1] = 1
                        self.grid[coordonnee_x][cordonnee_y - 1] = 1
              coordonnee_y+= 1
        coordonnee_x += 1
