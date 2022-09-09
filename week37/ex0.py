#Assigns a variable the value of user input, prints questions for user to answer, then waits for input
alder = int(input('Venligst indtast din alder i år: '))
#same as above
indkomst = int(input('Venligst indtast din årlige indkomst: '))
lånemængde = int(input('indtast ønskede lånemængde: '))
#Print all variables to terminal
print('Alder: ' + alder, 'Indkomst: ' + indkomst, 'Lånemægde: '+ lånemængde)

#Giving input other than integers will result in errors

if alder > 21 and indkomst > 300000:
    if lånemængde > 10*indkomst:
        print("Du kan IKKE blive godkendt som låner.")
    else:
        print("Du kan blive godkendt som låner!")