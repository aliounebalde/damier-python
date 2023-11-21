from tkinter import *
from random import randrange

def carre(x1,y1,x2,y2):
    "tracé d'un carre de longueur x"
    can.create_rectangle(x1,y1,x2,y2,width=2,fill=couleur)

def changeCouleur():
    "Changement aléatoire de la couleur du tracé"
    global couleur
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8)
    # => génère un nombre aléatoire de 0 à 7
    couleur = pal[c]

def figure():
    "dessiner une cible"
    can.delete(ALL)
    i=ligne=0
    
    x1=y1=0
    x2=y2=21
    nextLine=0
    espace=21
    while(ligne<10):
        
        while(i<100):
            carre(x1,y1,x2,y2)
            #pour mettre un saut vide de meme distance(se deplace de la longueur)
            x1=x2+espace
            #a partir de x1 on ajoute une long de espace 
            x2=x1+espace
            #longueur verticale
            y2=y1+espace
            i+=20

        ligne+=1
        nextLine+=20
        i=0
        #si ligne impaire on commence pas au debut
        if(ligne%2!=0):
            x1=espace+1
        #si paire on commence au debut
        else:
            x1=0
        #commence logueur carre apres
        y1=nextLine+1
        x2 = x1 + espace
        y2 = y1 + espace
        
        
couleur='black'
fen = Tk()
can = Canvas(fen, width =210, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
but1=Button(fen,text='Damier',command=figure)
but1.pack(side=LEFT,padx=3,pady=3)
bou3 = Button(fen,text='Autre couleur',command=changeCouleur)
bou3.pack(side=RIGHT,padx=3,pady=3)
fen.mainloop()