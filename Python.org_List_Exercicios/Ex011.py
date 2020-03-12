""""Altere o programa anterior, intercalando 3 vetores de 10 elementos cada."""

vetor1 = []
vetor2 = []

vetor1 = list(range(1,11))
vetor2 = list(range(1,11))
vetor3 = list(range(1,11))
vetor4 = list(range(1,11))

for num in range(10):
  vetor4.append(vetor1[num])
  vetor4.append(vetor2[num])
  vetor4.append(vetor3[num])
print(vetor4)