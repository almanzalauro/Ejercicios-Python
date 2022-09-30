#Practicando clases y objetos

class Coche:
        ruedas=4

        #constructor de cada instancia de la clase

        #metodos son los que serian "funciones()" para
        #atributos serian los "self.___"
        def __init__(self,color,aceleracion):
                self.color=color
                self.aceleracion=aceleracion
                self.velocidad=0

        def acelerar(self):
                self.velocidad=self.velocidad+self.aceleracion
                
        def frenar(self):
                v=self.velocidad+self.aceleracion

                if v<0:
                        v=0
                self.velocidad=v

auto1=Coche('Rojo',20)
print(auto1.color)
print(auto1.ruedas)

auto2=Coche('azul',6)
print(auto2.color)
print(auto2.ruedas)
