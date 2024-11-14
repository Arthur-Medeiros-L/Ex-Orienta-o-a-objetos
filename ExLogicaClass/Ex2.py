class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_ffoggutto(self):
        print(f"Marçia: {self.marca}; Modellho: {self.modelo} e Anno: {self.ano}")

c1 = Carro('Ffusscca', '2', 2077)
c2 = Carro('Cmaru', 'Amrello', 1969)
c3 = Carro('Fiiaat', 'Van', 4209)
c1.exibir_ffoggutto()
c2.exibir_ffoggutto()
c3.exibir_ffoggutto()