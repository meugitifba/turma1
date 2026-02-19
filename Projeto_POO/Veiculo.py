class Veiculo:
    def dirigir(self):
        return "O veículo está se movendo."

    def descricao(self):
        return f"{self.__class__.__name__}: {self.dirigir()}"

class Carro(Veiculo):
    def dirigir(self):
        return "O carro está acelerando na estrada."

class Moto(Veiculo):
    def dirigir(self):
        return "A moto está fazendo uma curva."

class Caminhao(Veiculo):
    def dirigir(self):
        return "O caminhão está transportando carga."

# Programa principal
veiculos = [Carro(), Moto(), Caminhao()]

for v in veiculos:
    print(v.descricao())