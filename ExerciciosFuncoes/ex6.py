'''
Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse exercício
'''

import random

def escolher_palavra():
    palavras = ["python", "programa", "desenvolvimento", "algoritmo", "computador"]
    return random.choice(palavras)

def exibir_palavra(palavra, letras_adivinhadas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            exibicao += letra
        else:
            exibicao += "_"
    return exibicao

def todas_adivinhadas(palavra, letras_adivinhadas):
    for letra in palavra:
        if letra not in letras_adivinhadas:
            return False
    return True

def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    letras_adivinhadas = []
    tentativas_erradas = 0
    max_tentativas = 6

    print("Bem-vindo ao jogo da forca!")

    while tentativas_erradas < max_tentativas:
        print(f"Palavra: {exibir_palavra(palavra_secreta, letras_adivinhadas)}")
        print(f"Tentativas restantes: {max_tentativas - tentativas_erradas}")
        
        tentativa = input("Digite uma letra: ").lower()

        if tentativa in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente outra.")
        elif tentativa in palavra_secreta:
            letras_adivinhadas.append(tentativa)
            print("Boa! Você acertou uma letra.")
            
            if todas_adivinhadas(palavra_secreta, letras_adivinhadas):
                print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
                break
        else:
            tentativas_erradas += 1
            print("Ops! A letra não está na palavra.")
        
        print()
    
    if tentativas_erradas == max_tentativas:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

if __name__ == "__main__":
    jogo_da_forca()