import Box2D as b2
import pygame
from Surface import Surface
from Bird import Bird
from Box import Box
from Pig import Pig
from PointsManager import PointsManager
class ContactListener(b2.b2ContactListener):

    def __init__(self, pointsManager, **kwargs):
        super().__init__(**kwargs)
        self.pointsManager = pointsManager


    def BeginContact(self, contact:b2.b2Contact):
        fixture1:b2.b2Fixture = contact.fixtureA
        fixture2:b2.b2Fixture = contact.fixtureB

        body1:b2.b2Body = fixture1.body
        body2:b2.b2Body = fixture2.body
        
        o1 = body1.userData
        o2 = body2.userData

        # Bird Collisions
        if isinstance(o2, Bird): 
            o1, o2 = o2, o1
        
        if isinstance(o1, Bird) and isinstance(o2, Box):
            print("xoquen bird box!")
            o1.birdCollided()
            o2.boxCollided()
            self.pointsManager.addPoints(10, False)

        if isinstance(o1, Bird) and isinstance(o2, Pig):
            o1.birdCollided()
            print(o1.getLinearVelocity().length)
            isKilled = o2.pigCollidedWithBird(o1.getLinearVelocity().length)

            if (isKilled == True):
                self.pointsManager.addPoints(150, True)
            if (isKilled == False):
                self.pointsManager.addPoints(10, False)

        if isinstance(o1, Bird) and isinstance(o2, Surface):
            o1.birdCollided()
            self.pointsManager.addPoints(5, False)

        # Pig Collisions - Excluding Bird
        if isinstance(o2, Pig): 
            o1, o2 = o2, o1

        if isinstance(o1, Pig) and isinstance(o2, Surface):
            isKilled = o1.pigCollidedWithSurf(o1.getLinearVelocity().length)
            if (isKilled == True):
                self.pointsManager.addPoints(50, True)
            if (isKilled == False):
                self.pointsManager.addPoints(20, False)
        pass

        if isinstance(o1, Pig) and isinstance(o2, Box):
            isKilled = o1.pigCollidedWithWall(o1.getLinearVelocity().length, o2.getLinearVelocity().length)

            if (isKilled == True):
                self.pointsManager.addPoints(100, True)
            if (isKilled == False):
                self.pointsManager.addPoints(50, False)
        pass

    def EndContact(self, contact:b2.b2Contact):
        pass
    def PreSolve(self, contact:b2.b2Contact, oldManifold:b2.b2Manifold,):
        pass
    def PostSolve(self, contact:b2.b2Contact, impulse:b2.b2ContactImpulse):
        pass