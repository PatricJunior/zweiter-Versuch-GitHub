import random
import time

#Beispielliste
musterliste1 = [random.randint(0,200) for _ in range (1000)]
musterliste2 = [random.randint(0,1000) for _ in range (300)]
musterliste3 = [random.randint(0,100000) for _ in range (10000) ]

#Tauschefunktion

def tausche(liste,a,b):
    liste[a], liste[b]  = liste[b], liste[a]
    return liste

# Selction Sort

def selectionsort (liste):
    for i in range (len(liste)):
        min = i
        for j in range (i+1, len(liste)):
           if liste[j] < liste[min]: 
             min = j
        tausche(liste,i,min)
    return liste


#insertion Sort

def insertionsort (liste):
    j=0
    for i in range(1,len(liste)):
        j=i
        while (j>0) and liste[j-1] > liste[j]:
            tausche(liste, j, j-1)
            j -=1
    return liste


#Mergesort

def mergesort(liste):
    if len(liste) <= 1:
        return liste
    arramitte = len(liste)//2
    arralinks = liste[:arramitte]
    arrarechts = liste[arramitte:]

    arralinks = mergesort(arralinks)
    arrarechts= mergesort(arrarechts)
    return merge(arralinks, arrarechts)

def merge (arralinks, arrarechts):
    neuarray = []
    i=j=0
    while i < len(arralinks) and j < len(arrarechts):
        if arralinks[i] < arrarechts[j]:
            neuarray.append(arralinks[i])
            i +=1
        else :
             neuarray.append(arrarechts[j])
             j +=1
    neuarray.extend(arralinks[i :])
    neuarray.extend(arrarechts[j :])
    return neuarray


# Benutzerfehler behebung
"""while True :
    auswahl = input("Wählen Sie bitte den Sortieralgorithmus Ihrer Wahl."+"\n" +"1- SELECTION SORT "+"\n" +"2- INSERTION SORT"+"\n" + "3- MERGE SORT" + "\n")
    try :
        auswahl = int(auswahl)
        if auswahl in [1,2,3] :
            break

    except ValueError:
        print (" Auswahl nicht unterstützt , versuchen Sie erneut !!")

if auswahl == 1:
    print(selectionsort(musterliste))
            
elif auswahl == 2:
    print(insertionsort(musterliste))
            
elif auswahl == 3:
    print(mergesort(musterliste))"""
            

# Zeit des Algorithms messen 

def bearbeitungszeit (sortieralgorithmus,musterliste):
    testcopy = musterliste.copy()

    startzeit = time.time()
    sortieralgorithmus(testcopy)
    endezeit = time.time()
    return f"Die  Liste braucht {endezeit-startzeit:.5f} Sekunden , um mit dem {sortieralgorithmus.__name__} Algortihmus sortiert zu werden !"


print( "\n" + "Für die liste musterliste1 = [random.randint(0,200) for _ in range (1000)] haben wir folgende Ergebnisse :"+ "\n")
print(bearbeitungszeit(mergesort,musterliste1))
print(bearbeitungszeit(selectionsort,musterliste1))
print(bearbeitungszeit(insertionsort,musterliste1)+ "\n")




print( "Für die liste musterliste2 = [random.randint(0,1000) for _ in range (300)] haben wir folgende Ergebnisse :"+ "\n")
print(bearbeitungszeit(mergesort,musterliste2) )
print(bearbeitungszeit(selectionsort,musterliste2))
print(bearbeitungszeit(insertionsort,musterliste2)+ "\n")



print( "Für die liste musterliste3 = [random.randint(0,100000) for _ in range (10000) ] haben wir folgende Ergebnisse :"+ "\n")
print(bearbeitungszeit(mergesort,musterliste3))
print(bearbeitungszeit(selectionsort,musterliste3))
print(bearbeitungszeit(insertionsort,musterliste3))







