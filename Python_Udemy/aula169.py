# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
# print(caminho)
diretorio, arquivo = os.path.split(caminho)
caminho_arquivo, extensao_arquivo = os.path.splitext(caminho)

# print(caminho_arquivo, extensao_arquivo)
# print(os.path.exists('C:\\Users\\efmiranda\\OneDrive - Tribunal de Justica de Sao Paulo\\Área de Trabalho\\Python_estudos\\Python_Udemy'))
# print(os.path.abspath('.'))
print(caminho)
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))


