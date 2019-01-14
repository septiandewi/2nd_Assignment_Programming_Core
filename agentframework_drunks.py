# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 21:56:07 2019

@author: Septian Dewi Cahyani
"""

import random
class Drunk():
#define condition of each drunk and setting up the environment. it defined the zero position and zero condition 
    def __init__ (self, city_map ,drunks, y, x, Id):
         if (x == None):
           self.x = random.randint(0,100)
         else:
           self.x = x
    
         if (y == None):
           self.y = random.randint(0,100)
         else:
           self.y = y
         if (x == None):
           self.Id = random.randint(0,100)
         else:
           self.Id = Id  
         self.city_map = city_map
         self.drunks = drunks
         self.path = 0 
#make the drunk move
    def move(self):        
        if random.random() < 0.5:
            self.y = (self.y + 5) % 288
        else:
            self.y = (self.y - 5) % 288
        if random.random() < 0.5:
            self.x = (self.x + 5) % 288
        else:
            self.x = (self.x - 5) % 288 
        
# making path
    def make_path(self): 
        if self.city_map[self.y][self.x] >= 0: 
            self.city_map[self.y][self.x] += 1 #add some colour to make footprint
            self.path += 1 
#stopping condition
    def stop(self):
        if self.city_map[self.y][self.x] == self.Id:
             self.y = (self.y + 0) 
        if self.city_map[self.y][self.x] == self.Id:
             self.x = (self.x + 0) 
        
        

