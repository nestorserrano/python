from functools import reduce
import os
import random

def normalize(s):
    replacements = (
        ("á","a"), 
        ("é","e"), 
        ("í","i"),  
        ("ó","o"),  
        ("ú","u") 
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def read():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.replace("\n",""))  
    word = random.choice(words)
    return normalize(word).upper()


def dibujo(counter):
    if counter == 1:        
        print('''









                                       ||
                                       ||
            ''')
    elif counter == 2:
        print('''






                      /  |   | \       ||
                         |   |         ||
                         /   \         ||
                                       ||
                                       ||
            ''')
    elif counter == 3:
        print('''



                        |_ o _|  /     ||
                          | |---/      ||
                        /|   |\        ||
                       / |   | \       ||
                         |   |         ||
                         /   \         ||
                                       ||
                                       ||
        ''')
    elif counter == 4:
        print('''


                        | o o |  |     ||
                        |_ Q _|  /     ||
                          | |---/      ||
                        /|   |\        ||
                       / |   | \       ||
                         |   |         ||
                         /   \         ||
                                       ||
                                       ||
        ''')
    elif counter == 5:
        print('''
                     ____________________
                        _______  |     ||
   Y O U    L O S T !!! | * * |  |     ||
                        |_ Q _|  /     ||
                          | |---/      ||
                        /|   |\        ||
                       / |   | \       ||
                         |   |         ||
                         /   \         ||
                                       ||
                                       ||
        ''')
    elif counter == 0:
        print('''
  
  
  
  
  
  
  
  
  
  
  
          ''')
    elif counter == -1:
        print('''
                     ____________________
                                 |     ||
   Y  O  U    W  I   N  !!!      |     ||
            _______              |     ||
            | o o |              |     ||
            |'---'|            (   )   ||
              | |               """    ||
          \ /|   |\ /                  ||
             |   |                     ||
             |   |                     ||
             /   \                     ||
        ''')      



def limpiar(palabra,size, counter):
    os.system("clear")    
    palabra="".join(palabra)   
    print("                    ".center(80,"="),end="\n")
    print(" ADIVINA LA PALABRA ".center(80,"="))    
    print("                    ".center(80,"="),end="\n")
    dibujo(counter)
    print("                  ",end="\n")
    if palabra.count == -1:        
        print("_" * size)
    else:                
        print(palabra)
    print("                  ",end="\n")


def perdido(word):
    print(f'Has Perdido... La palabra era: {word}',end="\n")            


def main():
    word=[]
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    word = read()  
    sizeword = len(word)    
    LIMIT = 5
    counter = 0
    sumar = False
    print(word)
    acert = []
    acert3 = []    
    ingresada = '' 
    acert4 = ''      
    limpiar("_ " * sizeword,sizeword,0)    
    while counter <= LIMIT:                          
        print("Tienes " + str(LIMIT-counter) + ", oportunidades",end="\n")  
        #print("Ingresadas: " + ingresada.upper())                                               
        print("")
        print("----------------------------------------------------")
        print("")
        option = input("Ingrese una Letra: ").upper()
        if len(option) > 1:
            if len(acert4) >= 1: 
                limpiar(acert4,sizeword,counter)  
            else:
                limpiar("_ " * sizeword,sizeword,counter)
            print("Debe ingresar una sola letra",end="\n")            
        elif len(option) == 0:
            if len(acert4) >= 1: 
                limpiar(acert4,sizeword,counter)  
            else:
                limpiar("_ " * sizeword,sizeword,counter)
            print("Debe escribir una letra",end="\n")        
        else:
            for letter in option:
                if letter not in letters:
                    if len(acert4) >= 1: 
                        limpiar(acert4,sizeword,counter)  
                    else:
                        limpiar("_ " * sizeword,sizeword,counter)
                    print("Debe Ingresar solo LETRAS",end="\n")
                    break
                else:    
                    if ingresada.count(option) >= 1:                
                        counter += 1
                        sumar = True
                        if counter >= LIMIT:                                            
                            limpiar(acert4,sizeword,5)  
                            print(f'La letra {option} ya fue ingresada, pierde su ultimo turno',end="\n")   
                            perdido(word)                                
                            exit()                
                        else:
                            limpiar(acert4,sizeword,counter)                   
                            print(f'La letra {option} ya fue ingresada, pierde un turno, te quedan {LIMIT-counter} intentos',end="\n")                                                                                       
                            break                            
                    else:                                        
                        ingresada = ingresada + option                                                          
                        acert = list(filter(lambda x: x == option,word))
                        acert=" ".join(acert) 
                        if len(acert) == 0:                
                            if sumar == False:
                                counter += 1  
                                limpiar(acert4,sizeword,counter)                                                     
                                if counter >= LIMIT:
                                    print(f'Letra no encontrada, ya no tiene mas intentos...',end="\n")                                   
                                    perdido(word)
                                    exit()                                                               
                                else:                                     
                                    if len(acert4) == 0: 
                                        limpiar("_ " * sizeword,sizeword,counter)
                                    else:
                                        limpiar(acert4,sizeword,counter)  
                                    print(f'Letra no encontrada, te quedan {LIMIT-counter} intentos',end="\n")
                                    break                                
                            else:
                                counter += 1
                                if counter >= LIMIT:
                                    print(f'Letra no encontrada, ya no tiene mas intentos...',end="\n")                                   
                                    perdido(word)
                                    exit()                                                               
                                else:     
                                    if len(acert4) == 0: 
                                        limpiar("_ " * sizeword,sizeword,counter)
                                    else:
                                        limpiar(acert4,sizeword,counter)  
                                    print(f'Letra no encontrada, te quedan {LIMIT-counter} intentos',end="\n")
                                    sumar == False                        
                                    break   
                        else:         
                            acert3 = []        
                            for i in word:                
                                for j in ingresada:                    
                                    if i == j:
                                        acert3 == acert3.append(i)     
                                        break 
                                for k in ingresada:
                                    if i != j:
                                        acert3 == acert3.append('_')
                                        break   
                    acert4 = " ".join(acert3)                
                    limpiar(acert4,sizeword,counter)       
                    if acert4 == " ".join(word):                      
                        limpiar(acert4,sizeword,-1)  
                        print(f'Has Ganado... La palabra era: {word} Felicidades',end="\n")                       
                        exit()                     
                    if counter >= LIMIT:
                        limpiar(acert4,sizeword,5)  
                        perdido(word)                            
                        exit()

if __name__ == "__main__":
    main() 