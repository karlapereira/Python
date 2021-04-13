from pessoa import Pessoa

# p1 = Pessoa()
# p1.nome = 'Luiz'

p1 = Pessoa('Karla', 25)
p2 = Pessoa('João', 32)

p1.comer('maçã')
p1.falar('POO')
p2.falar('Filmes')
p1.parar_comer()
p1.falar('POO')
p1.comer('bolo')
print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())