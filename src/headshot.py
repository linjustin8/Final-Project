# headshot.py
import requests
import pandas as pd
import numpy as np
from data import *

class Headshots:
    def __init__(self, player,points):
        self.player = player
        self.playerID = np.nan
        self.points = points
        self.dataf = dataframe_init()
        #self.playerID = self.getPlayerID(self.player)
        
    def getPlayerID(self, player): # prototype 1
        intValID = self.dataf.loc[self.dataf['playerName'] == player, 'playerID']
        # print(intValID)
        # likely gonna be done with hashset class
        return(intValID)
    
    def split_name(self):
        split = self.player.strip().split()
        firstname = split[0]
        lastname = split[-1] if len(split)>1 else "" # ensures the element accessed is actually the last name
        
        return firstname, lastname
    
    def downloadImage(self):
        localID = self.getPlayerID(self.player)
        response = requests.get(f"https://cdn.nba.com/headshots/nba/latest/1040x760/{localID}.png")

        firstname, lastname = self.split_name()
        if(response.status_code == 200):
            with open(f"assets/{firstname}_{lastname}.png", "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print("Image Downloaded")
        else: 
            print("Failed to Retrieve Image")
                
            