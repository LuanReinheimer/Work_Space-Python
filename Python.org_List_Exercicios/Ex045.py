"""Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa."""

listacarros = []
consumo_carros = []


for nome in range(0,3):
    nome = str(input(f'Digite o nome do {nome+1} carro: '))
    listacarros.append(nome)
    consumo = float(input(f'Digite o consumo do {nome} carro: '))
    consumo_carros.append(consumo)

for carro in range(0,3):
    print(f'Veiculo {carro +1}')
    print(f'Nome: {listacarros[carro]}')
    print(f'Km por litro: {consumo_carros[carro]}')

print('-'*30)
print(listacarros)
print(consumo_carros)