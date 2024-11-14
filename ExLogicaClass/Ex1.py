class Pessoa:
    def __init__(self, nome, idade): 
        self.nome = nome
        self.idade = idade
    def exibe_pessoas(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

p1 = Pessoa('Robertiçon', 3)
p2 = Pessoa('Mariante', 68)
p1.exibe_pessoas()
p2.exibe_pessoas()