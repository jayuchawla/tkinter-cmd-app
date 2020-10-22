import os
from tkinter import *
from tkinter import ttk

from DAO.UserDAO import UserDAO
from DAO.CommandDAO import CommandDAO
from DAO.LocationDAO import LocationDAO


class Root(Tk):
    def __init__(self, title):
        super(Root, self).__init__()
        self.title(title)
        self.minsize(640, 500)
        self.wm_iconbitmap("")
        self.loginUi()
        
        self.userDAO = UserDAO()

    def loginUi(self):
        self.usernameLabel = ttk.Label(self, text = "Username: ")
        self.usernameLabel.grid(column = 0, row  = 0)
        self.usernameInput = ttk.Entry(self, width = 30)
        self.usernameInput.grid(column = 1, row = 0)
        
        self.passwordLabel = ttk.Label(self, text = "Password: ")
        self.passwordLabel.grid(column = 0, row  = 1)
        self.passwordInput = ttk.Entry(self, width = 30)
        self.passwordInput.grid(column = 1, row = 1)
        
        self.loginButton = ttk.Button(self, text = "Login", command = lambda: self.login(self.usernameInput.get(), self.passwordInput.get()))
        self.loginButton.grid(column = 0, row = 2)

        self.errorLoginErrorLabel = ttk.Label(self, text = "")
        self.errorLoginErrorLabel.grid(column = 0, row = 3)

    def login(self, username, password):
        valid = self.userDAO.getUserByUsernameAndPassword(username, password)
        if valid == False:
            self.errorLoginErrorLabel.configure(text = "Invalid details!!", foreground = 'red')
        else:
            self.errorLoginErrorLabel.configure(text = "User logged in!!", foreground = 'green')
            self.ui()

    def ui(self):        
        self.commandLabel = ttk.Label(text = "Select command: ")
        self.commandLabel.grid(column = 0, row  = 5)
        self.comboBoxCommands = ttk.Combobox(self, width = 30)
        self.comboBoxCommands['values'] = CommandDAO().getAllCommandNames()
        self.comboBoxCommands.grid(column = 1, row = 5)
        
        self.locationLabel = ttk.Label(text = "Select location: ")
        self.locationLabel.grid(column = 0, row = 6)
        self.comboBoxLocations = ttk.Combobox(self, width = 30)
        self.comboBoxLocations['values'] = LocationDAO().getAllLocationNames()
        self.comboBoxLocations.grid(column = 1, row = 6)
        
        self.button = ttk.Button(self, text = "Click Me", command = lambda: self.buttonClick(CommandDAO().getCommandByName(self.comboBoxCommands.get()), LocationDAO().getLocationByName(self.comboBoxLocations.get())))
        #print(CommandDAO().getCommandByName(self.comboBoxCommands.get()), LocationDAO.getLocationByName(self.comboBoxLocations.get()))
        self.button.grid(column = 0, row = 7)

        self.label = ttk.Label(self, text = "")
        self.label.grid(column = 0, row = 7)

    def buttonClick(self, command, location):
        print(command, location)
        parsedLocation = self.locationParser(location)

        #self.label.configure(text = "You typed: " + parsedLocation)
        os.system('cmd /C "{} {}"'.format(command, parsedLocation))

    def locationParser(self, location):
        dirs = location.split("\\")
        loc = ""

        for i in range(len(dirs)-1):
            loc = loc + dirs[i] + "\\\\"
        loc+=dirs[len(dirs)-1]
        
        return loc