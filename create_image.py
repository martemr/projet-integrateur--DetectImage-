import numpy as np
from PIL import Image as im
import csv
from numpy import genfromtxt
import os, random
from tensorflow import keras 
from keras.datasets import mnist



# Fonction qui genere la matrice de données mnist
def generate_img_matrix(nb_matrix, Y_train, X_train) :
    result = [] 
    for i in range(len(nb_matrix)) :
        result.append([]) # crée une ligne dans le tableau, sinon les cases existent pas
        for j in range(len(nb_matrix[0])):
            result[-1].append(random_number(nb_matrix[i][j], Y_train, X_train)) # -1 veut dire dernière ligne generee
    print(result) #A ETUUUUUUUUUUUUDIIIIIIIIIIIIIIIIIIIIIIIIIIIIER pour pouvoir bien faire img complete [[array([[]..[]], dtype=uint8)...array([[]..[]], dtype=uint8)]]
    return result

#Fonction qui genere l'image complete
def generate_img_complete(img_matrix) :
    data = im.fromarray(np.asarray(img_matrix))
    data.save("test.png")
    return data

#Fonction qui recupere une image mnist au hasard en fonction du nombre qu'on recherche
def random_number(number, Y_train, X_train) :
    train_filter = np.where(Y_train == number ) # recupere les indices des labels egaux à number
    train_filter=np.array(train_filter[0]) # train_filter est un tuple dont on ne veut que le premier element (correspond au tableau des indices)
    randomIndex=np.random.choice(train_filter) # choisit un indice au hasard dans la liste de ceux qui correspondent
    randomNumber=X_train[randomIndex] # retourne l'image correspondant à cet indice
    return randomNumber




# Chargement des données de mnist
(train_X, train_y), (test_X, test_y) = mnist.load_data() # x=images y=labels
# Lecture du fichier .has
nb_matrix = genfromtxt('./Hashi_Puzzles/100/Hs_16_100_25_00_001.has', skip_header=1, delimiter='  ')
# Création de la matrice avec des données mnist
img_matrix = generate_img_matrix(nb_matrix, train_y, train_X)
# Création de l'image complète (assemblage des morceaux de la matrice)
img = generate_img_complete(img_matrix)








