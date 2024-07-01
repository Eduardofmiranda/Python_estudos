# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enederecos = []
        
    def inserir_endereco(self, rua, numero):
        self.enederecos.append(Endereco(rua, numero))
        
    def listar_enderecos(self):
        for endereco in self.enederecos:
            print(endereco.rua, endereco.numero)
        
class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua 
        self.numero = numero
        
cliente1 = Cliente('Maria')      
cliente1.inserir_endereco('Av. Brasil', 65)
cliente1.inserir_endereco('Av. B', 623)
cliente1.listar_enderecos()
