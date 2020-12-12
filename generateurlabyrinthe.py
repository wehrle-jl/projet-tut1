# -*- coding: utf-8 -*-
import turtle as tt 
import random as rm
tafullvaleur=[0,1]
colonelignevaleur=[]
posibilite=[]

def genlab(tafullvaleur):
    taille,finlignecolone,debutcolone,debutligne,case = setup(tafullvaleur)
    gengrid(debutligne,taille,case,debutcolone,finlignecolone)
    setupcase(case,taille)
    score=genchemin(case,taille)
    return(score)

def setup(tafullvaleur):
    tt.tracer(0,0)#montre les action une fois qu'il a tout fini #temps pour génére un 100² (1,1)=18mn (100,0)=30/25s // (200,0)=19/18s // (500,0) 13s // (1000,0)=10 // (0,0)=6s pour un 500² 6mn 36s plantage mémoire a 145k  
    debutcolone=debutligne = -250
    finlignecolone=250
    taille=None
    while taille ==None: #on empeche l'appuie sur le bouton cancel
        taille =(tt.numinput("donnez","donnez un nombre pour un carré",35,minval=5,maxval=100)) #35 de base et bloqué entre 5 et 100
    taille =int(taille) # empéche les flotant
    #taille = int(input("ici :"))
    case=500/taille
    tafullvaleur.append(taille)
    tafullvaleur.append(case)
    tafullvaleur.append(0)
    tt.pu()
    return taille,finlignecolone,debutcolone,debutligne,case

def gengrid (ligne,taille,case,colone,finlignecolone):
    tt.goto(ligne,ligne)
    for i in range (0,taille+1):
        tt.pd()
        tt.goto(colone,finlignecolone)# fait une colone debas en haut
        colone = colone+case # se décale pour une nouvelle colone
        tt.pu()
        tt.goto(colone,ligne) # se décale pour une nouvelle colone
    tt.goto(ligne,ligne)
    colone=ligne
    for i in range (0,taille+1):
        tt.pd()
        tt.goto(finlignecolone,colone) # fait une ligne de gauche a droite
        colone = colone+case # se décal pour une nouvelle ligne
        tt.pu()
        tt.goto(ligne,colone) # se décal pour une nouvelle ligne

def setupcase(case,taille):
    for i in range (1,taille+1):
        for j in range (1,taille+1):
            colonelignevaleur.append([i,j,0]) #créer un tableau de la forme [colone, ligne, 0][colone, ligne+1, 0]....[colone+n,ligne+n,0]
    tt.goto(-225,-225)
    
def genchemin(case,taille): 
    ligncolon=lignecolonmax=0
    valeurchemin=valeurcheminmax=1
    conteur=1
    colonelignevaleur[0][2]=1
    tt.color("white") # color de fond pour pouvoir d'étruire les mur
    while conteur <=(taille*taille)-1 : # s'arréte quand on a ballayé toute les case
        posibilite=[]
        while len(posibilite)==0: # s'arréte si on a au moin une possibilité
            li=colonelignevaleur[ligncolon][1]
            co=colonelignevaleur[ligncolon][0] 
            if ligncolon < taille**2-taille: # empéche l'erreur index out of range
                if colonelignevaleur[ligncolon+taille] == [co+1,li,0]: #vérifie si la case a droite est libre
                    posibilite.append(1) #droite
                    ccdr=ligncolon+taille
            if ligncolon <taille**2-1: #empéche l'erreur index out of range
                if colonelignevaleur[ligncolon+1] == [co,li+1,0]: #vérifie si la case au dessu est libre
                    posibilite.append(2) #haute
                    cco=ligncolon+1
            if colonelignevaleur[ligncolon-taille] == [co-1,li,0]: #vérifie si la case a gauche est libre
                posibilite.append(3) #gauche
                ccg=ligncolon-taille
            if colonelignevaleur[ligncolon-1] == [co,li-1,0]:#vérifie si la case en dessou est libre
                posibilite.append(4) #bas
                ccb=ligncolon-1
            if len(posibilite)==0: # si aucune case n'est libre (cul de sa atteint)
                if ligncolon < taille**2-taille:# empéche l'erreur index out of range
                    if colonelignevaleur[ligncolon+taille] == [co+1,li,valeurchemin-1]: #vérifie si la case a droite est la case précédant
                        ligncolon=ligncolon+taille
                if ligncolon <taille**2-1:# empéche l'erreur index out of range
                    if colonelignevaleur[ligncolon+1] == [co,li+1,valeurchemin-1]: #vérifie si la case au dessu est la case précédant
                        ligncolon=ligncolon+1
                if colonelignevaleur[ligncolon-taille] == [co-1,li,valeurchemin-1]: #vérifie si la case a gauche est la case précédant
                    ligncolon=ligncolon-taille
                elif colonelignevaleur[ligncolon-1] == [co,li-1,valeurchemin-1]: #vérifie si la case en desssou est la case précédant
                    ligncolon=ligncolon-1   
                valeurchemin =valeurchemin-1    
        deplacement = rm.choice(posibilite)#choisie un posibilité au hasard
        valeurchemin=valeurchemin+1 # on avance
        conteur=conteur+1 # on a ballayer une case supllémentaire
        print(conteur) # montre l'avancement
        if deplacement == 2: #haut
            tt.pu()
            tt.goto(-250+colonelignevaleur[ligncolon][0]*case,-250+colonelignevaleur[ligncolon][1]*case)#se place dans le coin haut droit
            tt.pd()
            tt.goto(-250+(colonelignevaleur[ligncolon][0]-1)*case,-250+(colonelignevaleur[ligncolon][1])*case) #repasse sur le mur du haut de droite a gauche
            ligncolon=cco
        elif deplacement == 1:#droite
            tt.pu()
            tt.goto(-250+(colonelignevaleur[ligncolon][0])*case,-250+(colonelignevaleur[ligncolon][1])*case) #se place dans le coin haut droit
            tt.pd()
            tt.goto(-250+colonelignevaleur[ligncolon][0]*case,-250+(colonelignevaleur[ligncolon][1]-1)*case)  #repasse sur le mur de droite de haut en bas
            ligncolon=ccdr
        elif deplacement == 4:#bas
            tt.pu()
            tt.goto((-250-case)+colonelignevaleur[ligncolon][0]*case,(-250-case)+colonelignevaleur[ligncolon][1]*case)#se place dans le coin bas gauche
            tt.pd()
            tt.goto((-250-case)+(colonelignevaleur[ligncolon][0]+1)*case,(-250-case)+colonelignevaleur[ligncolon][1]*case)  #repasse sur le mur du bas de gauche a droite
            ligncolon=ccb
        elif deplacement == 3:#gauche
            tt.pu()
            tt.goto((-250-case)+colonelignevaleur[ligncolon][0]*case,(-250-case)+colonelignevaleur[ligncolon][1]*case) #se place dans le coin bas gauche
            tt.pd()
            tt.goto((-250-case)+(colonelignevaleur[ligncolon][0])*case,(-250-case)+(colonelignevaleur[ligncolon][1]+1)*case) #repasse sur le mur de gauche de bas en haut
            ligncolon=ccg
        colonelignevaleur[ligncolon][2]=valeurchemin
        if valeurchemin > valeurcheminmax :
            valeurcheminmax=valeurchemin
            lignecolonmax=ligncolon
    tt.pu()
    tt.tracer(1,1) #repasse a la vitesse de base (montre une 1*action toute les 1*action)
    tt.color("black") # mes la tortue en noir
    tt.shapesize(case/50) # mes la tortue a la taille du tableau
    tt.goto(-250+(case/2)+(case/4),-250+(case/2))  # place la tortue dans la case bas droite
    ligncolon=0
    info=tt.Turtle() # créer une tortue info
    score=tt.Turtle() #créer une tortue score
    info.pu()
    score.pu()
    info.goto(0,325) 
    score.goto(0,275) # déplacement des tortue
    info.write("nombre minimum : {}".format(colonelignevaleur[lignecolonmax][2]-1), align = "center", font = ("Arial", 15, "bold"))
    info.goto(0,300)
    info.write("position de la cas la plus loin :{} {}".format(colonelignevaleur[lignecolonmax][0],colonelignevaleur[lignecolonmax][1]), align = "center", font = ("Arial", 15, "bold"))
    tafullvaleur.append(lignecolonmax)
    score.write("nombre de déplacement : 0", align = "center", font = ("Arial", 15, "bold")) # écrit toute les donné
    info.ht()
    score.ht() # on cache les tortue
    fill(lignecolonmax,case) # on remplie la case de fin 
    return(score) # on renvoit la tortu score

def fill(lignecolonmax,case):
    fill=tt.Turtle() # on creer un tortue fill
    fill.ht()
    fill.pu() # on la cache et on l'empeche d'écrire
    fill.color("red")
    fill.goto((-250+colonelignevaleur[lignecolonmax][0]*case)-1,(-250+colonelignevaleur[lignecolonmax][1]*case)-1)#on se place dans le coin haut droit
    fill.begin_fill()
    fill.goto((-250+colonelignevaleur[lignecolonmax][0]*case)-1,(-250+colonelignevaleur[lignecolonmax][1]*case)-case+1) # on vas au coin haut gauche
    fill.goto((-250+colonelignevaleur[lignecolonmax][0]*case)-case+1,(-250+colonelignevaleur[lignecolonmax][1]*case)-case+1) # on vas au coin bas gauche
    fill.goto((-250+colonelignevaleur[lignecolonmax][0]*case)-case+1,(-250+colonelignevaleur[lignecolonmax][1]*case)-1) # on vas au coin bas droite
    fill.goto(-250+colonelignevaleur[lignecolonmax][0]*case-1,-250+colonelignevaleur[lignecolonmax][1]*case-1) #on retourne au coin haut droit pour finir le fill
    fill.end_fill() # on a fait systémétiquement -1 pour pouvoir toujour voir les murs
    
    
def droite (tafullvaleur,colonelignevaleur,score):
    ligncolone = tafullvaleur[0]# on récupére le numéro d'index de la case actuel
    deplaceposs = tafullvaleur[1] # la valeur du chemin pour connaitre les déplacemnt possible
    decalagecolone=tafullvaleur[2] # le nombre de case pour changer de colone
    decalageposition=(tafullvaleur[3]) # le nombre pour se déplace de millieu de case en milllieu de case
    if tt.xcor()+decalageposition<250: #empéche l'erreur index out of range 
        if colonelignevaleur[ligncolone+decalagecolone][2]+1 == deplaceposs or colonelignevaleur[ligncolone+decalagecolone][2]-1 == deplaceposs : # on vérifie si on peut aller a droite
            tt.goto(tt.xcor()+decalageposition,tt.ycor())  # on déplace la tortue
            ligncolone=ligncolone+decalagecolone
            tafullvaleur[1]=colonelignevaleur[ligncolone][2] #on rentre la nouvelle valleur de déplacement
            tafullvaleur[0]=ligncolone # le nouveau numéro de case
            aftermove(tafullvaleur,colonelignevaleur,score)
            
def haut (tafullvaleur,colonelignevaleur,score):  
    ligncolone = tafullvaleur[0]# on récupére le numéro d'index de la case actuel
    deplaceposs = tafullvaleur[1] # la valeur du chemin pour connaitre les déplacemnt possible
    decalageposition=(tafullvaleur[3]) # le nombre pour se déplace de millieu de case en milllieu de case
    if tt.ycor()+decalageposition<250: # empéche l'erreur out of range
        if colonelignevaleur[ligncolone+1][2]+1 == deplaceposs or colonelignevaleur[ligncolone+1][2]-1 == deplaceposs :
            tt.goto(tt.xcor(),tt.ycor()+decalageposition)  # on déplace la tortue
            ligncolone=ligncolone+1
            tafullvaleur[1]=colonelignevaleur[ligncolone][2] #on rentre la nouvelle valleur de déplacement
            tafullvaleur[0]=ligncolone # le nouveau numéro de case
            aftermove(tafullvaleur,colonelignevaleur,score)
        
def gauche (tafullvaleur,colonelignevaleur,score):
    ligncolone = tafullvaleur[0]# on récupére le numéro d'index de la case actuel
    deplaceposs = tafullvaleur[1] # la valeur du chemin pour connaitre les déplacemnt possible
    decalagecolone=tafullvaleur[2] # le nombre de case pour changer de colone
    decalageposition=(tafullvaleur[3]) # le nombre pour se déplace de millieu de case en milllieu de case
    if colonelignevaleur[ligncolone-decalagecolone][2]+1 == deplaceposs or colonelignevaleur[ligncolone-decalagecolone][2]-1 == deplaceposs :
        tt.goto(tt.xcor()-decalageposition,tt.ycor())  # on déplace la tortue
        ligncolone=ligncolone-decalagecolone
        tafullvaleur[1]=colonelignevaleur[ligncolone][2] #on rentre la nouvelle valleur de déplacement
        tafullvaleur[0]=ligncolone # le nouveau numéro de case
        aftermove(tafullvaleur,colonelignevaleur,score)
        
def bas (tafullvaleur,colonelignevaleur,score):
    ligncolone = tafullvaleur[0]# on récupére le numéro d'index de la case actuel
    deplaceposs = tafullvaleur[1] # la valeur du chemin pour connaitre les déplacemnt possible
    decalageposition=(tafullvaleur[3]) # le nombre pour se déplace de millieu de case en milllieu de case
    if colonelignevaleur[ligncolone-1][2]+1 == deplaceposs or colonelignevaleur[ligncolone-1][2]-1 == deplaceposs :
        tt.goto(tt.xcor(),tt.ycor()-decalageposition)  # on déplace la tortue
        ligncolone=ligncolone-1
        tafullvaleur[1]=colonelignevaleur[ligncolone][2] #on rentre la nouvelle valleur de déplacement
        tafullvaleur[0]=ligncolone # le nouveau numéro de case
        aftermove(tafullvaleur,colonelignevaleur,score)

def aftermove (tafullvaleur,colonelignevaleur,score):
    tafullvaleur[4]=tafullvaleur[4]+1 # augmente le score de 1
    score.clear() # efface ce qua écrit la tortu score
    score.write("nombre de déplacement : {}".format(tafullvaleur[4]), align = "center" , font = ("Arial", 15, "bold"))# on récrit le score
    if tafullvaleur[0] == tafullvaleur[5]: # si la case de victoire est atteint 
       reset(tafullvaleur) # on recommence

def effacer(tafullvaleur):
    tt.clear() #on efface tt
    tt.reset() # on le reset
    ecran.reset() # on reset l'ecrant
    tafullvaleur.clear() # on efface le tableau tafullvaleur
    tafullvaleur.append(0) # on remet les valeur de base
    tafullvaleur.append(1) # parreil
    colonelignevaleur.clear() # on reset colonelignevaleur
    
def reset(tafullvaleur): # reset = effacer + recommencer
    effacer(tafullvaleur)
    genlab(tafullvaleur)
    
ecran=tt.Screen()
ecran.setup(width=0.5, height=1.0, startx=1, starty=0) #génere un écrant da la moitier de la largeur et de hauteur max
tt.speed(0) # vitesse max
score=genlab(tafullvaleur)
if __name__ == "__main__":
    tt.listen()
    tt.onkey(lambda : droite(tafullvaleur,colonelignevaleur,score),'Right')
    tt.onkey(lambda : haut(tafullvaleur,colonelignevaleur,score),'Up')
    tt.onkey(lambda : bas(tafullvaleur,colonelignevaleur,score),'Down')
    tt.onkey(lambda : gauche(tafullvaleur,colonelignevaleur,score),'Left')
    tt.onkey(lambda : effacer(tafullvaleur),'c')
    tt.onkey(lambda : reset(tafullvaleur),'r')
    #tt.onkey(tst,'t')
    tt.mainloop()
    tt.bye()