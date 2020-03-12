"""faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores."""

# Declando listas
vetor1 = []
vetor2 = []
# Utilizando o range para adicionar numeros de 1 a 10 dentro das listas
vetor1 = list(range(1,11))
vetor2 = list(range(1,11))

# Declarando um vetor para intercalar os dois primieros dentro dele
vetor3 = []

# Usando um for in range para fazer a intercalação dos vetor1 e vetor2 no vetor 3

for num in range(10):
  vetor3.append(vetor1[num])
  vetor3.append(vetor2[num])

# Imprimindo o vetor3
print(vetor3)