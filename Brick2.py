# coding=utf-8

class Brick(): 
    #attribut de classe un dictionnaire de couleurs
    COLORS = {1: "#ffB6C1", 2: "#3B2077", 3: "#0000ff", 4: "#00ff00", 5: "#ffff00", 6: "#ff8000", 7: "#ff0000", 8: "#ffB6C1"}

    def __init__(self, x, y, hits):# le constructeur
        self.w = 75 # attribut longueur
        self.h = 20 # attribut largeur
        self.pos = PVector(x, y) # attribut position
        self.hits = hits #attribut clé pour la couleur
        self.col = Brick.COLORS[hits] # la couleur
        
    # méthode pour afficher la brique
    def display(self):
        fill(self.col)
        stroke("#ffffff") # couleur du bord
        strokeWeight(2)# épaisseur des bords
        rect(self.pos.x, self.pos.y, self.w, self.h)
