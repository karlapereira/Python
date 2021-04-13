"""
Associacao - Usa | Agregacao - Tem | Composição - É dono | Herança - É
"""

from classes_associacao import Escritor
from classes_associacao import Caneta
from classes_associacao import MaquinaDeEscrever
from classes_agregacao import CarrinhoDeCompras, Produto
# from classes_composicao import Cliente
from classes_heranca import *

## Associacao
escritor = Escritor('Karla')
caneta = Caneta('Bic')
#maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
#escritor.ferramenta.escrever()

## Agregacao
carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Caneca', 20)
p3 = Produto('Sapato', 200)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

# carrinho.lista_produto()
# print(carrinho.soma_total())

## Composicao
"""
cliente1 = Cliente('Karla', 25)
cliente1.insere_endereco('SRS', 'MG')
cliente1.insere_endereco('O.F.', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Lara', 21)
cliente2.insere_endereco('P.A.', 'MG')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 18)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()

print('##############################')
"""

## Herança

c1 = Cliente('Karla', 25)
c1.falar()
c1.comprar()
a1 = Aluno('Ana', 28)
a1.falar()
a1.estudar()
