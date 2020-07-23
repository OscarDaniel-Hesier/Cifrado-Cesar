# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 14:51:51 2020

@author: Hesier
"""


#-------------------------------------------------------
#-------------------CIFRADO CESAR-----------------------
#-------------------------------------------------------        
#libreria para importar alfabeto completo, para no utilizar mucho codigo    
import string
"""empaquetamos todo las letras en una variable dentro de una lista"""

alfabeto = list(string.ascii_lowercase)

def cifrado_cesar(alfabeto,n,texto):  #n= numero desplazamientos
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra) #index nos permite ingresar al indice de un elemeto en especifico
            indice_cesar = indice_actual + n
            if indice_cesar > 25:
                indice_cesar -=25 #si fuera 27 se le resta 25 y pasa a ser la posiscion que equivale a "c" la tercera pocision del alfabeto
            texto_cifrado += alfabeto[indice_cesar] # texto_cifrado va ser igual a la letra del alfabeto que tome el indice_cesar    
        else:
            texto_cifrado += letra      # si no esta el caracter especial solamente se agrega al cifrado
    return texto_cifrado

#2 EJEMPLO CIFRADO-DECODIFICACION

def decodificar(alfabeto,n,texto):  #n= numero desplazamientos
    texto_decodificado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_cesar = alfabeto.index(letra) 
            indice_original = indice_cesar - n
            if indice_original < 0:
                indice_original +=25 
            texto_decodificado += alfabeto[indice_original]     
        else:
            texto_decodificado += letra      
    return texto_decodificado

resp = "si"
while(resp !="no"):
    print("----Programa para cifrar una frase con el algoritmo Cesar----")
    frase = input("Ingresa la frase a cifrar: ")
    frase = frase.lower()
    frase_cifrada = cifrado_cesar(alfabeto, 3, frase)
    print("(1)--el mensaje cifrado es: ", frase_cifrada)
    frase_decodificada = decodificar(alfabeto,3,frase_cifrada)
    print("(2)--De nuevo, el mensaje decifrado es: ", frase_decodificada)
    resp = input("Desea cifrar otra frase(si/no)?: ")
    resp = resp.lower()