# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:45:21 2020

@author: user
"""

from Connection.DbConnection import DbConnection
import mysql.connector as mc

class CommandDAO:
    def __init__(self):
        self.db = DbConnection()
        self.dbcursor = self.db.getCursor()  
    
    def insertCommand(self, command):
        pass
    
    def removeCommand(self, command):
        pass
    
    def getAllCommands(self):
        try:
            query = "select * from command"
            self.dbcursor.execute(query)
            result = self.dbcursor.fetchall()
            if not result:
                return False 
            return result    
        except mc.Error as e:
            print(e.msg)
    
    def getAllCommandNames(self):
        list_of_commands = self.getAllCommands()
        listOfCommandNames = []
        for command in list_of_commands:
            listOfCommandNames.append(command[1])
        return listOfCommandNames
        
    
    def getCommandByName(self, commandName):
        try:
            query = "select * from command where com_name='{}'".format(commandName)
            self.dbcursor.execute(query)
            result = self.dbcursor.fetchall()
            if not result:
                return False 
            return result[0][2]    
        except mc.Error as e:
            print(e.msg)
            