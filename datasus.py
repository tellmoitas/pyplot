import matplotlib.pyplot as plt

dados = open("original.csv").readlines()
x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append(int(linha[0]))
        y.append(int(linha[1]))

plt.plot(x,y)
plt.title("Crescimento populacão brasileira")
plt.xlabel("Ano")
plt.ylabel("Polulação x 100.000.000")
plt.show()