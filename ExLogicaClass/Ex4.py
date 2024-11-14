class Animal:
    def emitir_som(self):
        pass

class Cachorro(Animal):
    def emitir_som(self):
        print ("Quale paraça, faz isso naop auau")
    
class Gato(Animal):
    def emitir_som(self):
        print("nao nao irmao, maiu maiu")

cachorro = Cachorro()
gato = Gato()
cachorro.emitir_som()
gato.emitir_som()
        
    