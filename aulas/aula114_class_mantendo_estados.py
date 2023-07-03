
# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, modelo, filmando=False):
        self.nome = nome
        self.modelo = modelo
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} {self.modelo} já está filmando 📹')

        self.filmando = True

class Tripe:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


c1 = Camera('Sony', 'A50')
t1 = Tripe('Aliexpress', 'Fulero')



print(c1.filmando)
print(c1.nome)
print(c1.modelo)
print(type(c1))

c1.filmar()
c1.filmar()

print(t1.marca)
print(t1.modelo)

print(f'Estou filmando com minha {c1.nome} {c1.modelo}, porém meu tripé é {t1.modelo}, da {t1.marca}')
