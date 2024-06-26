#heap.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#default initiator to grab information from csv and organize it into a map
def dataframe_init():
    #use ../assets/___.csv or assets/___.csv depending on files
    filename = '../assets/boxscore_scrape.csv'
    filename_head = '../assets/NBA_Player_IDs.csv'

    originaldf = pd.read_csv(filename) #maintain original dataframe
    modifieddf=originaldf.copy() #modifying new dataframe

    #cleaning up dataframe by assigning NaN to games players didn't play
    modifieddf['PTS']=modifieddf['PTS'].replace('Did Not Play',-1)
    modifieddf['PTS']=modifieddf['PTS'].replace('Not With Team',-1)
    modifieddf['PTS']=modifieddf['PTS'].replace('Did Not Dress',-1)
    modifieddf['PTS']=modifieddf['PTS'].replace('Player Suspended',-1)

    modifieddf=modifieddf.iloc[1:] #remove header

    #organize csv by player name, and organize each player by points
    modifieddf=modifieddf.sort_values(by=['playerName'],ascending=[True])

    #new dataframe, following ISO-8859-1 update
    player_head = pd.read_csv(filename_head,encoding='ISO-8859-1')
    player_head = player_head.iloc[:,[4,6]]

    originaldf = (final_df_frame(modifieddf,player_head))
    cool_row = {'teamName': 'LeGoat', 'playerName': 'Aman Kapoor', 'PTS': 101, 'NBAID': '11111'}
    originaldf.loc[len(originaldf)]=cool_row

    return originaldf
#------------------------------------------------------------------------------------------

def final_df_frame(df1,df2):

    #create local dataframe to be returned, and create new column with all rows NaN
    df_base = df1
    df_base['NBAID']=np.nan
    df_base['NBAID'] = df_base['NBAID'].astype(str)

    #creating a dictionary by zipping two columns and assinging key-value pairs
    dictionary_of_IDs = dict(zip(df2['NBAName'],df2['NBAID']))

    #manually populating a hashmap (dictionary) alternative
    hashmap_of_IDs = {}

    #alternative to itterows that saves some time and space
    for column in df2.itertuples(index=False):
        hashmap_of_IDs[column.NBAName] = column.NBAID

    similarity_map = df_base['playerName'].map(hashmap_of_IDs)
    df_base['NBAID'] = similarity_map.astype(str)

    """ 
            slow nested for loop approach to assigning new values
            could be used as an example for increased efficiency of vectorized approach
    for (key,value) in dictionary_of_IDs.items():
        indexs = df_base[df_base['playerName'] == key].index
        for i in indexs :
            df_base.loc[i,'BBRefID'] = value
            print('in')
        print('out')
        """


    return (df_base)
#-----------------------------------------------------------------------------
def checker(df,player):
    return df['playerName'].str.strip().str.lower().isin([player]).any()
#------------------------------------------------------------------------------
def getID(df,player):
    pass
#------------------------------------------------------------------------------
def list_o_point_create(df, name):
    df['playerName'] = df['playerName'].str.lower().str.strip()
    df_by_name = df[df['playerName'] == name]
    lisp=df_by_name['PTS'].tolist()
    return lisp
#------------------------------------------------------------------------------
def visualizer (listerine,overunder,playerName):

    fig, axe = plt.subplots(figsize=(5,5))
    sns.set(style="whitegrid")

    sns.histplot(listerine,bins =np.unique(listerine), ax=axe, color='#27aeef')
    axe.axvline(x=overunder, color='#f46a9b', linestyle='solid', linewidth=1.5)
    axe.set_title('Plot of PPG Count')
    axe.set_xlabel('Points per Game')
    axe.set_ylabel('count')
    plt.savefig(f'../assets/{playerName}_graph.png')

    return

    """
    plt.hist(listerine,bins=np.unique(listerine),color='black')
    plt.show()
    """

def list_o_name_create(df):
    #implement a Nary tree or B+ tree, not sure yet
    pass

"""
#will be removed, using to check code
if __name__ == "__main__":
    dataframe_init()
"""