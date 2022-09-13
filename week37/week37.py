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

# #Prints the first 10 titles
# for i in range(10):
#     print(titel[i])

# #Prints tiles with rating < 8.0 in the first 80 titles
# for i in range(80):
#     if vurdering[i] < 8.0:
#         print(titel[i])

# #Print all titles above a length of 10 chars
# for i in titel:
#     if(len(i) > 10):
#         print(i)

# #Counts number of metascores above 80
# count = 0
# for i in metascore:
#     if(i > 80):
#         count = count+1
# print(count)

# #Printer hvor mange titler der er i listen
# print(len(titel))

# #Printer listen
# print(titel)

# #Print bestemt titel hvis den er der
# for i in titel:
#     if(i == 'The Lion King'):
#         print(i)

# for i in instruktører:
#     if(i == 'Wes Anderson'):
#         print(i)

counter = 0
for i in range(len(instruktører)):
    if instruktører[i] == 'Hayao Miyazaki':
        counter += 1
print(counter)

print(instruktører.count('Hayao Miyazaki'))