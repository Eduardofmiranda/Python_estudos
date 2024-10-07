# type:ignore
tabuleiro = [['.' for _ in range(8)] for _ in range(8)]

def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
        
# Definir as peças nas posições iniciais
tabuleiro[0] = ["R", "N", "B", "Q", "K", "B", "N", "R"]  # Primeira fileira - Torres, Cavalos, Bispos, Rainha e Rei
tabuleiro[1] = ["P" for _ in range(8)]  # Segunda fileira - Peões
tabuleiro[6] = ["p" for _ in range(8)]  # Sétima fileira - Peões (peças brancas)
tabuleiro[7] = ["r", "n", "b", "q", "k", "b", "n", "r"]  # Oitava fileira - Torres, Cavalos, Bispos, Rainha e Rei (peças brancas)


def jogar_xadrez(tabuleiro, origem, destino):
    linha_origem, coluna_origem = origem
    linha_destino, coluna_destino = destino 
    
    peca = tabuleiro[linha_origem][coluna_origem]
           
    tabuleiro[linha_destino][coluna_destino] = peca    
    

    
    tabuleiro[linha_origem][coluna_origem] = '.' # type:ignore
    
# Agora imprimir novamente o tabuleiro
imprimir_tabuleiro(tabuleiro)

jogar_xadrez(tabuleiro, (1, 0), (5, 0))
print()


imprimir_tabuleiro(tabuleiro)
