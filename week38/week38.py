# Forestil jer vi har lavet et program til en vejrstation, som nu løbende måler temperatur og relativ luftfugtighed. Der er dog et lille problem. Målingerne er engang imellem ret ved siden af…

# Derfor skal i nu i teams prøve at fikse dette problem med funktioner.

# Kravene er som følger:

# Temperatur skal være mellem 0 og 50 grader.
# Den relative luftfugtighed skal være mellem 20% og 90%.
# Lav en funktion der tager ét input-parameter: temperatur.
# Den skal med operatorer og conditions tjekke om temperaturen er i den korrekte range.
# Hvis ikke, skal den printe en advarsel om at temperaturen er udenfor det godkendte område. Dette gøres i en return statement sidst i koden (se eksempler under opgaveinformation ovenfor).
# Gentag trin 1-3, men med luftfugtighed i stedet for temperatur. Husk at funktionen nu skal tage 2 input-parametre.
# Kør funktionen med forskellige kombinationer af temperatur og luftfugtigheds input-parametre for at tjekke om den gør det den skal.

def temp_humidity_checker(temp, humidity):
    if(temp < 0 or temp > 50):
        print("Temparatur er udenfor det godkendte område")
    if(humidity < 20 or humidity > 90):
        print("Luftfugtighed er udenfor det godkendte område")
    return


temp_humidity_checker(30,90)