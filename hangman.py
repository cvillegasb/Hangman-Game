from palabras import palabras
import random
import string

def obt_random_word(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()

def hangman():
    adivinar_palabra = obt_random_word(palabras)
    letra_adivinar = set(adivinar_palabra)
    alfabeto = set(string.ascii_uppercase)
    letras_usadas = set()

    vidas = 6

    while len(letra_adivinar) > 0 and vidas > 0:
        
        print('Tu has usado estas letras: ', ''.join(letras_usadas))
        lista_de_palabras = [letra if letra in letras_usadas else '-' for letra in adivinar_palabra]

        print('Palabra actual: ', ''.join(lista_de_palabras))
    
        usar_letra = input('Adivina una letra: ').upper()
        if usar_letra in alfabeto - letras_usadas:
            letras_usadas.add(usar_letra)
            if usar_letra in letra_adivinar:
                letra_adivinar.remove(usar_letra)
                print('')
            else:
                vidas = vidas - 1
                print('\nTu letra', usar_letra, 'No esta en la palabra')
    
        elif usar_letra in letras_usadas:
            print('\nYa has usado esta letra. Por favor, usa una nueva')

        else:
            print('\nCaracter invalido. Por facor, usa un caracter valido')

    if vidas == 0:
        print('Has muerto. La palabra fue ', adivinar_palabra)
    else:
        print('Yeah Adivinaste la palabra', adivinar_palabra)
    

if __name__ == '__main__':
    hangman()
