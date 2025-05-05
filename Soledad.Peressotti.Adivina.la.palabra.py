import random

def selec_palab(): # se define una lista de posibles palabras
    palab = ["comando", "bibioteca", "diagrama", "inteligencia", "diccionario", "python", "software"]
    return random.choice(palab)

def mostrar_palab_ocu(palabra, letras_acertadas): # funcion para mostrar la palabra oculta y las letras acertadas y no
    return "".join([letra if letra in letras_acertadas else "_" for letra in palabra]) # las no acertadas se muestran con guion bajo "_"

def jugar():
    palabra = selec_palab() # el programa selecciona una palabra
    letras_acertadas = set() # para guardar las letras acertadas sin repeticiones       
    letras_no_acertadas = set()  # para guardar las letras no acertadas sin repeticiones
    vidas = 6 # se le otorga al jugador 6 vidas

    print("¡HOLA! TE INVITO A JUGAR\n") 

    while vidas > 0:
        print(f"ADIVINA LA PALABRA:", mostrar_palab_ocu(palabra, letras_acertadas)) # muestra la palabra oculta
        print(f"Letras incorrectas: {' '.join(letras_no_acertadas)}") # muestra las letras incorrectas
        print(f"Vidas que te quedan: {vidas}") # muestra las vidas que quedan

        letra = input("Ingresa una letra: ").lower() # solicita ingresar una letra
        print()
    
        if letra in palabra:
            letras_acertadas.add(letra) # si la letra esta, se muestra en la palabra oculta
            if all(l in letras_acertadas for l in palabra): # si se adivinan todas la letras se avisa que gano
                print(f"¡Lo lograste! Adivinaste la palabra: {palabra}\n")
                break
        else:
            letras_no_acertadas.add(letra) # si agrega una letra incorrecta
            vidas -= 1                     # se resta una vida

    else:
        print(f"¡Ups! Esta vez no salió. La palabra era: {palabra}\n") # si pierde todas las vidas se muestra la palabra correcta

def main():
    while True:
        jugar()                                                              # si responde si, puede repetir 
        respuesta = input("¿Querés intentarlo de nuevo? (s/n): ").lower()    # el juego las veces que quiera.
        if respuesta != 's':                # si responde no, o cualquier otra letra,
            print("¡Gracias por jugar!\n")  # el programa muestra un saludo y se cierra.
            break
main()












