
class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
p1 = Pessoa('Gustavo', 29)
p2 = Pessoa('Ariely', 29)
p3 = Pessoa('Larissa', 25)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print(p3.get_ano_nascimento())