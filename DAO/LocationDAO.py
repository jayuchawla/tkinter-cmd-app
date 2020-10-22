# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:21:30 2020

@author: user
"""
from Connection.DbConnection import DbConnection
import mysql.connector as mc

class LocationDAO:
    def __init__(self):
        self.db = DbConnection()
        self.dbcursor = self.db.getCursor()         
        
    def getAllLocations(self):
        try:
            query = "select * from location"
            self.dbcursor.execute(query)
            result = self.dbcursor.fetchall()
            if not result:
                return False 
            return result    
        except mc.Error as e:
            print(e.msg)
            
    def getAllLocationNames(self):
        list_of_locations = self.getAllLocations()
        listOfLocationNames = []
        for location in list_of_locations:
            listOfLocationNames.append(location[1])
        return listOfLocationNames
    
    def getLocationByName(self, locationName):
        try:
            query = "select * from location where loc_name='{}'".format(locationName)
            self.dbcursor.execute(query)
            result = self.dbcursor.fetchall()
            if not result:
                return False 
            return result[0][2]    
        except mc.Error as e:
            print(e.msg)
            
if __name__ == "__main__":
    print(LocationDAO().getLocationByName("Downloads Video ct"))