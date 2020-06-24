
class Damier:

    def longueur(self,n=-1):
        while n <= 0 or n > 1000:
              n = int(input("Longueur du damier : "))
              if n > 1000:
                print("Valeur trop grande , mettez une valeur entre 0 et 1000")
              if n < 0:
                print("Valeur trop petite , mettez une valeur entre 0 et 1000")
        return n

    def largeur (self,p=-1):
        while p <= 0 or p > 1000:
              p = int(input("Largeur du damier : "))
              if p > 1000:
                print("Valeur trop grande , mettez une valeur entre 0 et 1000")
              if p < 0:
                print("Valeur trop petite , mettez une valeur entre 0 et 1000")
        return p

    def nom(self,x=-1):
        x = input("Entrer le nom de la simulation : ")
        return x