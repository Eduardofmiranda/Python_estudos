# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
from typing import Any


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'Está Chamando', self.phone)
        return 1234

call1 = CallMe('11990141574')
retorno = call1('Eduardo Miranda')
print(retorno)
