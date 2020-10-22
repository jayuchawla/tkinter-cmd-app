# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:26:04 2020

@author: user
"""

class Location:
    def __init__(self, loc_id, loc_name, location):
        self.loc_id = loc_id
        self.loc_name = loc_name
        self.location = location
    
    def getLocation(self):
        return self.location
    
    def getLocationName(self):
        return self.loc_name