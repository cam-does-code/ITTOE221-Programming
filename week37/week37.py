import pandas as pd

''' 
Data hentet fra Kaggle - https://www.kaggle.com/datasets/tarundalal/animated-movies-imdb
Det er data over top 85 animationsfilm på IMDB.
'''
table = pd.read_csv("https://raw.githubusercontent.com/AllanMisasa/UCL-Code/main/Python/TopAnimatedImDb.csv")
print(table.head())

'''
Lister ud fra forskellige datapunkter. 
Titel - Titel på film
Vurdering - Alle ratings på IMDB
Metascore - Metascore - samlet score fra Metacritic
År - Årstal for udgivelse af filmen
Antal_vurderinger - Antal ratings på IMDB
Instruktører - Hvem der var instruktør på filmen
'''
titel = list(table['Title'])
vurdering = list(table['Rating'])
metascore = list(table['Metascore'])
år = list(table['Year'])
antal_vurderinger = list(table['Votes'])
instruktører = list(table['Director'])

#Prints the first 10 titles
for i in range(10):
    print(titel[i])

#Prints tiles with rating < 8.0 in the first 80 titles
for i in range(80):
    if vurdering[i] < 8.0:
        print(titel[i])