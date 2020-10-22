# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:05:46 2020

@author: user
"""

class Command:
    def __init__(self, com_id, com_name, command):
        self.com_id = com_id
        self.com_name = com_name
        self.command = command
        
    def getCommandName(self):
        return self.com_name
    def getCommand(self):
        return self.command