import utils
import pygame
import numpy as np
import Box2D as b2

#Gestor de punts, que guarda la informació de cada nivell en un array de diccionaris. 
class PointsManager:

    #Funció per inicialitzar el gestor de puntuacions amb els nivells buits
    def __init__ (self, numLevels):
        self.levels_points = []
        self.currentLevel = None

        for i in range(numLevels):
            level = {
                "number" : i+1,
                "points" : 0,
                "stars": 0,
                "pigs_tokill" : 0,
                "pigs_killed" : 0,
                "level_passed" : False,
                "th_1_stars" : 0,
                "th_2_stars" : 0,
                "th_3_stars" : 0
            }
            self.levels_points.append(level)

    #Funció per reinicialitzar els valors del nivell actual
    def restartLevel(self, currentLevel, pigstoKill, th_1_stars, th_2_stars, th_3_stars):
        self.currentLevel = currentLevel
        level = {
                "number" : currentLevel+1,
                "points" : 0,
                "stars": 0,
                "pigs_tokill" : pigstoKill,
                "pigs_killed" : 0,
                "level_passed" : False,
                "th_1_stars" : th_1_stars,
                "th_2_stars" : th_2_stars,
                "th_3_stars" : th_3_stars        
        }

        self.levels_points[currentLevel] = level

    #Funció per afegir nous punts al nivell, indicant si els punts són donats per algun enemic eliminat
    def addPoints(self, newPoints, pigIsKilled):

        self.levels_points[self.currentLevel]["points"] += newPoints
        self.levels_points[self.currentLevel]["stars"] = self.getUpdatedStars(self.currentLevel)

        if (pigIsKilled == True):
            self.levels_points[self.currentLevel]["pigs_killed"] += 1
     
            if (self.levels_points[self.currentLevel]["pigs_killed"] == self.levels_points[self.currentLevel]["pigs_tokill"]):
                self.levels_points[self.currentLevel]["level_passed"] = True

    
    #Funció per saber quantes estrelles té el nivell seleccionat
    def getUpdatedStars(self, currentLevel):
        currentPoints = self.levels_points[currentLevel]["points"]

        if (currentPoints < self.levels_points[currentLevel]["th_1_stars"]):
            return 0

        if (currentPoints >= self.levels_points[currentLevel]["th_1_stars"] and currentPoints < self.levels_points[currentLevel]["th_2_stars"]):
            return 1
        
        if (currentPoints >= self.levels_points[currentLevel]["th_2_stars"] and currentPoints < self.levels_points[currentLevel]["th_3_stars"]):
            return 2

        if(currentPoints >= self.levels_points[currentLevel]["th_3_stars"]):
            return 3


    #Getter de punts
    def getPoints(self, currentLevel):
        return self.levels_points[currentLevel]["points"]
    
    #Getter d'estrelles
    def getStars(self, currentLevel):
        return self.levels_points[currentLevel]["stars"]
    
    def setPassed(self, currentLevel):
        self.levels_points[currentLevel]["level_passed"] = True

    #Funció per comprovar si el nivell actual s'ha completat
    def checkIfLevelIsPassed(self, currentLevel, birdsAvailable):
        if (birdsAvailable == False):
            self.levels_points[currentLevel]["level_passed"] = True

        return self.levels_points[currentLevel]["level_passed"]




