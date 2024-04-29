import random

def palavra_aleatoria():
    palavras = ['Eduardo', 'Miranda', 'Teste',]
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_correta):
    for letra in palavra:
        if letra in letras_correta:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def jogar_forca():
    palavra = palavra_aleatoria()
    letra_correta = []
    letras_erradas_chutadas = []
    tentativas = 6

    print('Bem-vindo ao Jogo da Forca!')
    print('Adivinha a palavra')
    mostrar_palavra(palavra, letra_correta)

    while tentativas > 0:
        palpite = input('Digite uma letra: ').lower()

        if palpite in letra_correta or palpite in letras_erradas_chutadas:
            letras_erradas_chutadas.append(palpite)
            print('Voce ja tentou essa letra')
            continue
        elif palpite in palavra:
            letra_correta.append(palpite)
            letras_erradas_chutadas.append(palpite)
            print('Ótimo! Essa letra está na palavra.')
        else:
            tentativas -= 1
            letras_erradas_chutadas.append(palpite)
            print('Essa letra não está na palavra, voce tem mais ', tentativas,'tentativas')
            

        mostrar_palavra(palavra, letra_correta)

        if '_' not in ''.join([letra if letra in letra_correta else '_' for letra in palavra]):
            print("Parabéns! Você ganhou!")
            break
    
    if '_' in ''.join([letra if letra in letra_correta else '_' for letra in palavra]):
        print("Você perdeu! A palavra era:", palavra)
        

if __name__ == "__main__":
    jogar_forca()

jogar_forca()