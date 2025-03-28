class Carro:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.ligado = False  # Atributo de estado
        self._velocidade = 0  # Atributo privado

    def acelerar(self, incremento):
        self._velocidade += incremento
        print(f"{self.modelo} acelerou para {self._velocidade} km/h")

    def mover(self):
        # Método genérico que será sobrescrito
        pass

# Exemplo de uso
meu_carro = Carro("Toyota", "Corolla", "Preto", 2022)





        

