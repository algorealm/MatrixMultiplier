def matrice(nbLignes, nbColonnes):
    matrice = [None] * nbLignes
    for x in range(nbLignes):
        matrice[x] = [0] * nbColonnes
    for i in range(nbLignes):
        for t in range(nbColonnes):
            matrice[i][t] = input()
    print(matrice)
    return matrice

def matriceVide(nbLignes, nbColonnes): #matrice vide pour ajouter des 
    matrice = [None] * nbLignes        #des elements par la suite
    for x in range(nbLignes):
        matrice[x] = [0] * nbColonnes
    return matrice


def multmatrices(nbLignes1, nbColonnes1, nbLignes2, nbColonnes2):
    mat1 = matrice(nbLignes1, nbColonnes1)
    mat2 = matrice(nbLignes2, nbColonnes2)
    matResultante = matriceVide(nbLignes1, nbColonnes2) #selon la definition des produits de matrices
    for i in range(nbLignes1):
        for t in range(nbColonnes2):
            for x in range(nbColonnes1):
                matResultante[i][t] = int(mat1[i][x]) * int(mat2[x][t]) + int(matResultante[i][t])
    return matResultante    
 
multmatrices(
    int(input('Nombre de lignes de la premiere matrice')),
    int(input('Nombre de colonnes de la premiere matrice')),
    int(input('Nombre de lignes de la deuxieme matrice')),
    int(input('Nombre de colonnes de la deuxieme matrice'))
)

    
