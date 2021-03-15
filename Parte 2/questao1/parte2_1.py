# -*- coding: utf-8 -*-
"""
@author: JESS
"""

class Animal():
    _som = ''
    
    def emitirSom(self):
        return self._som
        
class Gato(Animal):
    _som = 'Miau'
    
class Cachorro(Animal):
    _som = 'Auau'
    
def atualizaHistorico(historico):
        historico.append([entrada, som])
        print(som)
    
def imprimeHistorico(historico):
    for linha in historico:
        print(linha[0], linha[1])
    
if __name__ == '__main__':
    
    cat = Gato()
    dog = Cachorro()
    historico = []
    som = ''

    while True:
        entrada = str(input())

        if not entrada!='historico':
            imprimeHistorico(historico)
            break
        elif entrada == '1':
            som = cat.emitirSom()
            atualizaHistorico(historico)
        elif entrada == '2':
            som = dog.emitirSom()
            atualizaHistorico(historico)
                    
            